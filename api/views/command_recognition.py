from underthesea import word_sent
from api.views import config
import paho.mqtt.publish as publish

class CommandRecognition(object):
    def __init__(self, sentence = ''):
        self.commands = config.COMMANDS
        self.locations = config.LOCATIONS
        self.objects = config.OBJECTS
        self.sentence = sentence
        self.host = "mqtt.koor.io"
        self.topic = "5aa1171bda0970019aad7c6a.koor.io/devices/5abfbaec95392e04569ece8c"

    def __split_sentence(self, delimiter = ' '):
        return self.sentence.lower().split(delimiter)

    def __split_command_sentences(self, wsents_arr):
        split_commands = []
        # Split to separate command
        indexs = []
        for i in range(len(wsents_arr)):
            if wsents_arr[i] in self.commands:
                indexs.append(i)
        indexs.append(len(wsents_arr))
        for i in range(len(indexs) - 1):
            split_commands.append(wsents_arr[indexs[i] : indexs[i + 1]])
        return split_commands

    def __sentences_segmentation(self, sent):
        return word_sent(sent)

    def __bigrams_detect(self, wsents):
        wsents_copy = wsents
        for i in range(len(wsents) - 1):
            temp = wsents[i] + ' ' + wsents[i + 1]
            if temp in self.commands or temp in self.objects or temp in self.locations:
                wsents_copy[i] = temp
                wsents_copy[i + 1] = ''
        return wsents_copy

    def __join_words(self, word_arr):
        return ' '.join(word_arr)

    def __join_commands(self):
        split_sentences = self.__split_command_sentences(self.__split_sentence())
        split_commands = []
        for sent in split_sentences:
            cmd = self.__join_words(sent[1:])
            cmd_segmented = self.__sentences_segmentation(cmd)
            bigram = self.__bigrams_detect(cmd_segmented)
            bigram.insert(0, sent[0])
            split_commands.append(bigram)
        return split_commands

    def detect_iot_commands(self):
        split_commands = self.__join_commands()
        result = []
        msgs = []
        for command in split_commands:
            temp = {
                'command': [],
                'objects': [],
                'locations': [],
            }
            temp_cmd = ""
            for word in command:
                if word in self.commands:
                    temp['command'].append(word)
                    temp_cmd += str(config.CMDS_MAPPING[word])
                if word in self.objects:
                    temp['objects'].append(word)
                if word in self.locations:
                    temp['locations'].append(word)
                    temp_cmd += str(config.PINMODE_MAPPING[word])
            result.append(temp)
            msgs.append({
                'topic' : self.topic,
                'payload' : temp_cmd
            })
        publish.multiple(msgs, hostname=self.host)
        return result

