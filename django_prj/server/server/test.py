import django
import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings_tmp")
django.setup()


from rest_framework.request import QueryDict, MultiValueDict
import re
from types import List

isListReg = re.compile(r'\w+\[([0-9]+)\](.*)$')

def _recursive_parse(obj:Dict, qdict, prefix):
    if obj == None:
        obj = {prefix: []}
    elif obj[prefix] == None:
        obj[prefix] = []

    regex = re.compile(r'^%s\[([0-9]+)\](.*)$' % re.escape(prefix))

    for field, value in qdict.items():
        match = regex.match(field)
        if not match:
            continue
        index, key = match.groups()
        print('---', index, key)
        print('')
        index = int(index)
        if isListReg.match(key):

        elif not key:
            obj[index] = value
        elif isinstance(obj.get(index), dict):
            obj[index][key] = value
        else:
            obj[index] = MultiValueDict({key: [value]})

def _parse_list(dictionary, prefix='', default=None):
    """
    代替 html.parse_html_list()
    解决 不能解析 'sentencesForeign[0][en]': ['hello'], 'sentencesForeign[0][cn]': ['你好']
    """
    ret = {}
    regex = re.compile(r'^%s\[([0-9]+)\](.*)$' % re.escape(prefix))
    for field, value in dictionary.items():
        match = regex.match(field)
        if not match:
            continue
        print('--- field', field)
        print('--- value', value)
        index, key = match.groups()
        print('---', index, key)
        print('')
        index = int(index)
        if not key:
            ret[index] = value
        elif isinstance(ret.get(index), dict):
            ret[index][key] = value
        else:
            ret[index] = MultiValueDict({key: [value]})

    print('--- ret', ret)
    # return the items of the ``ret`` dict, sorted by key, or ``default
    return [ret[item] for item in sorted(ret)] if ret else default

if __name__ == '__main__':
    qset = QueryDict('id=9&content=阿阿斯蒂芬&sentencePatternForeign[0][id]=4&sentencePatternForeign[1][id]=4&sentencePatternForeign[0][content]=a little&sentencePatternForeign[0][paraphraseSet][0][id]=22&sentencePatternForeign[0][paraphraseSet][0][interpret]=一些&sentencePatternForeign[0][paraphraseSet][0][partOfSpeech]=adj.&sentencePatternForeign[0][paraphraseSet][0][sentencePatternForeign]=4&sentencePatternForeign[0][paraphraseSet][0][sentenceSet][0][id]=24&sentencePatternForeign[0][paraphraseSet][0][sentenceSet][0][en]=a little water&sentencePatternForeign[0][paraphraseSet][0][sentenceSet][0][cn]=一些水&sentencePatternForeign[0][paraphraseSet][0][sentenceSet][0][paraphraseForeign]=22')
    print('---', qset)
    ret = _parse_list(qset, prefix='sentencePatternForeign', default=None)
    print(ret)
