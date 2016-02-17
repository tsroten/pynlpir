# -*- coding: utf-8 -*-
"""Part of speech mapping constants and functions for NLPIR/ICTCLAS.

This module is used by :mod:`pynlpir` to format segmented words for output.

"""
from __future__ import unicode_literals
import logging


logger = logging.getLogger('pynlpir.pos_map')

#: A dictionary that maps part of speech codes returned by NLPIR to
#: human-readable names (English and Chinese).
POS_MAP = {
    'n': ('名词', 'noun', {
        'nr': ('人名', 'personal name', {
            'nr1': ('汉语姓氏', 'Chinese surname'),
            'nr2': ('汉语名字', 'Chinese given name'),
            'nrj': ('日语人名', 'Japanese personal name'),
            'nrf': ('音译人名', 'transcribed personal name')
        }),
        'ns': ('地名', 'toponym', {
            'nsf': ('音译地名', 'transcribed toponym'),
        }),
        'nt': ('机构团体名', 'organization/group name'),
        'nz': ('其它专名', 'other proper noun'),
        'nl': ('名词性惯用语', 'noun phrase'),
        'ng': ('名词性语素', 'noun morpheme'),
    }),
    't': ('时间词', 'time word', {
        'tg': ('时间词性语素', 'time morpheme'),
    }),
    's': ('处所词', 'locative word'),
    'f': ('方位词', 'noun of locality'),
    'v': ('动词', 'verb', {
        'vd': ('副动词', 'auxiliary verb'),
        'vn': ('名动词', 'noun-verb'),
        'vshi': ('动词"是"', 'verb 是'),
        'vyou': ('动词"有"', 'verb 有'),
        'vf': ('趋向动词', 'directional verb'),
        'vx': ('行事动词', 'performative verb'),
        'vi': ('不及物动词', 'intransitive verb'),
        'vl': ('动词性惯用语', 'verb phrase'),
        'vg': ('动词性语素', 'verb morpheme'),
    }),
    'a': ('形容词', 'adjective', {
        'ad': ('副形词', 'auxiliary adjective'),
        'an': ('名形词', 'noun-adjective'),
        'ag': ('形容词性语素', 'adjective morpheme'),
        'al': ('形容词性惯用语', 'adjective phrase'),
    }),
    'b': ('区别词', 'distinguishing word', {
        'bl': ('区别词性惯用语', 'distinguishing phrase'),
    }),
    'z': ('状态词', 'status word'),
    'r': ('代词', 'pronoun', {
        'rr': ('人称代词', 'personal pronoun'),
        'rz': ('指示代词', 'demonstrative pronoun', {
            'rzt': ('时间指示代词', 'temporal demonstrative pronoun'),
            'rzs': ('处所指示代词', 'locative demonstrative pronoun'),
            'rzv': ('谓词性指示代词', 'predicate demonstrative pronoun'),
        }),
        'ry': ('疑问代词', 'interrogative pronoun', {
            'ryt': ('时间疑问代词', 'temporal interrogative pronoun'),
            'rys': ('处所疑问代词', 'locative interrogative pronoun'),
            'ryv': ('谓词性疑问代词', 'predicate interrogative pronoun'),
        }),
        'rg': ('代词性语素', 'pronoun morpheme'),
    }),
    'm': ('数词', 'numeral', {
        'mq': ('数量词', 'numeral-plus-classifier compound'),
    }),
    'q': ('量词', 'classifier', {
        'qv': ('动量词', 'verbal classifier'),
        'qt': ('时量词', 'temporal classifier'),
    }),
    'd': ('副词', 'adverb'),
    'p': ('介词', 'preposition', {
        'pba': ('介词“把”', 'preposition 把'),
        'pbei': ('介词“被”', 'preposition 被'),
    }),
    'c': ('连词', 'conjunction', {
        'cc': ('并列连词', 'coordinating conjunction'),
    }),
    'u': ('助词', 'particle', {
        'uzhe': ('着', 'particle 着'),
        'ule': ('了／喽', 'particle 了/喽'),
        'uguo': ('过', 'particle 过'),
        'ude1': ('的／底', 'particle 的/底'),
        'ude2': ('地', 'particle 地'),
        'ude3': ('得', 'particle 得'),
        'usuo': ('所', 'particle 所'),
        'udeng': ('等／等等／云云', 'particle 等/等等/云云'),
        'uyy': ('一样／一般／似的／般', 'particle 一样/一般/似的/般'),
        'udh': ('的话', 'particle 的话'),
        'uls': ('来讲／来说／而言／说来', 'particle 来讲/来说/而言/说来'),
        'uzhi': ('之', 'particle 之'),
        'ulian': ('连', 'particle 连'),
    }),
    'e': ('叹词', 'interjection'),
    'y': ('语气词', 'modal particle'),
    'o': ('拟声词', 'onomatopoeia'),
    'h': ('前缀', 'prefix'),
    'k': ('后缀', 'suffix'),
    'x': ('字符串', 'string', {
        'xe': ('Email字符串', 'email address'),
        'xs': ('微博会话分隔符', 'hashtag'),
        'xm': ('表情符合', 'emoticon'),
        'xu': ('网址URL', 'URL'),
        'xx': ('非语素字', 'non-morpheme character'),
    }),
    'w': ('标点符号', 'punctuation mark', {
        'wkz': ('左括号', 'left parenthesis/bracket'),
        'wky': ('右括号', 'right parenthesis/bracket'),
        'wyz': ('左引号', 'left quotation mark'),
        'wyy': ('右引号', 'right quotation mark'),
        'wj': ('句号', 'period'),
        'ww': ('问号', 'question mark'),
        'wt': ('叹号', 'exclamation mark'),
        'wd': ('逗号', 'comma'),
        'wf': ('分号', 'semicolon'),
        'wn': ('顿号', 'enumeration comma'),
        'wm': ('冒号', 'colon'),
        'ws': ('省略号', 'ellipsis'),
        'wp': ('破折号', 'dash'),
        'wb': ('百分号千分号', 'percent/per mille sign'),
        'wh': ('单位符号', 'unit of measure sign'),
    }),
}


def _get_pos_name(pos_code, names='parent', english=True, pos_map=POS_MAP):
    """Gets the part of speech name for *pos_code*."""
    pos_code = pos_code.lower()  # Issue #10
    if names not in ('parent', 'child', 'all'):
        raise ValueError("names must be one of 'parent', 'child', or "
                         "'all'; not '%s'" % names)
    logger.debug("Getting %s POS name for '%s' formatted as '%s'." %
                 ('English' if english else 'Chinese', pos_code, names))
    for i in range(1, len(pos_code) + 1):
        try:
            pos_key = pos_code[0:i]
            pos_entry = pos_map[pos_key]
            break
        except KeyError:
            if i == len(pos_code):
                logger.warning("part of speech not recognized: '%s'"
                               % pos_code)
                return None  # Issue #20
    pos = (pos_entry[1 if english else 0], )
    if names == 'parent':
        logger.debug("Part of speech name found: '%s'" % pos[0])
        return pos[0]
    if len(pos_entry) == 3 and pos_key != pos_code:
        sub_map = pos_entry[2]
        logger.debug("Found parent part of speech name '%s'. Descending to "
                     "look for child name for '%s'" % (pos_entry[1], pos_code))
        sub_pos = _get_pos_name(pos_code, names, english, sub_map)
        pos = pos + sub_pos if names == 'all' else (sub_pos, )
    name = pos if names == 'all' else pos[-1]
    logger.debug("Part of speech name found: '%s'" % repr(name)
                 if isinstance(name, tuple) else name)
    return name


def get_pos_name(code, name='parent', english=True):
    """Gets the part of speech name for *code*.

    :param str code: The part of speech code to lookup, e.g. ``'nsf'``.
    :param str name: Which part of speech name to include in the output. Must
        be one of ``'parent'``, ``'child'``, or ``'all'``. Defaults to
        ``'parent'``. ``'parent'`` indicates that only the most generic name
        should be used, e.g. ``'noun'`` for ``'nsf'``. ``'child'`` indicates
        that the most specific name should be used, e.g.
        ``'transcribed toponym'`` for ``'nsf'``. ``'all'`` indicates that all
        names should be used, e.g. ``('noun', 'toponym',
        'transcribed toponym')`` for ``'nsf'``.
    :param bool english: Whether to return an English or Chinese name.
    :returns: ``str`` (``unicode`` for Python 2) if *name* is ``'parent'`` or
        ``'child'``. ``tuple`` if *name* is ``'all'``.

    """
    return _get_pos_name(code, name, english)
