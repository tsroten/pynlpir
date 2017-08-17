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
    'g': ('专有名词', 'proper noun', {
        'ga': ('国家或者地区官方媒体', 'national media', {
            'gaas': ('亚洲经济通讯社或亚洲新闻通讯社', 'asia media'),
            'gaau': ('澳联社', 'austrilia media'),
            'gacb': ('拉美社', 'latin america media'),
            'gacn': ('新华社或中新社', 'china media'),
            'gaes': ('埃新社', 'egypt media'),
            'gafr': ('法新社', 'france media'),
            'gagm': ('德新社', 'germany media'),
            'gahk': ('中评社或中通社', 'hongkong media'),
            'gaid': ('印度联合新闻社', 'india media'),
            'gain': ('安塔拉', 'indonesia media'),
            'gait': ('安莎社', 'italy media'),
            'gajp': ('时事社', 'japan media'),
            'gakr': ('韩联社', 'south korean media'),
            'gakrn': ('朝中社', 'north korean media'),
            'game': ('中东社', 'middle east media'),
            'gars': ('俄联社、俄新社或国际文传电讯社', 'russia media'),
            'gatw': ('中国经济通讯社或中央社', 'taiwan media'),
            'gauk': ('路透社', 'UK media'),
            'gaus': ('合众国际社或美联社', 'US media'),
            'gayr': ('伊通社', 'iran media'),
        }),
        'gjtgj': ('交通工具', 'vehicle'),
        'gms': ('美食', 'food'),
        'gn': ('新闻报纸', 'news', {
            'gnan': ('安徽报纸', 'news in anhui'),
            'gnbj': ('北京报纸', 'news in beijin'),
            'gncq': ('重庆报纸', 'news in chongqin'),
            'gndq': ('广州报纸', 'news in guanzhou'),
            'gnfj': ('福建报纸', 'news in fujian'),
            'gngd': ('广东报纸', 'news in guandong'),
            'gngs': ('甘肃报纸', 'news in gansu'),
            'gngx': ('广西报纸', 'news in guanxi'),
            'gngz': ('贵州报纸', 'news in guizhou'),
            'gnhan': ('海南报纸', 'news in hainan'), 
            'gnheb': ('河北报纸', 'news in hebei'),
            'gnhen': ('河南报纸', 'news in henan'),
            'gnhk': ('香港报纸', 'news in hongkong'),
            'gnhl': ('黑龙江报纸', 'news in heilongjiang'),
            'gnhub': ('湖北报纸', 'news in hubei'),
            'gnhun': ('湖南报纸', 'news in hunan'),
            'gnjl': ('吉林报纸', 'news in jilin'),
            'gnjs': ('江苏报纸', 'news in jiangsu'),
            'gnjx': ('江西报纸', 'news in jiangxi'),
            'gnln': ('辽宁报纸', 'news in liaoning'),
            'gnnx': ('宁夏报纸', 'news in ningxia'),
            'gnsa': ('陕西报纸', 'news in shan3xi'),
            'gnsc': ('四川报纸', 'news in sichuan'),
            'gnsd': ('山东报纸', 'news in shandong'),
            'gnsh': ('上海报纸', 'news in shanghai'),
            'gnsx': ('山西报纸', 'news in shanxi'),
            'gntj': ('天津报纸', 'news in tianjin'),
            'gntw': ('台湾报纸', 'news in taiwan'),
            'gnxj': ('新疆报纸', 'news in xinjiang'),
            'gnxz': ('西藏报纸', 'news in xizang'),
            'gnyn': ('云南报纸', 'news in yunnan'),
            'gnzj': ('浙江报纸', 'news in zhejiang'),
            'gnqg': ('全国报纸', 'news in china'),
        }),
        'grjyy': ('软件应用', 'software and application'),
        'gr': ('广播电台', 'radio', {
            'grc': ('城市广播电台', 'radio in city'),
            'grqg': ('全国广播电台', 'radio in nation'),
            'grs': ('省广播电台', 'radio in province'),
        }),
        'gt': ('电视台', 'tv station', {
            'gtc': ('城市电视台', 'tv station in city'),
            'gthk': ('香港电视台', 'tv station in hongkong'),
            'gtqg': ('全国电视台', 'tv station in china'),
            'gts': ('省电视台', 'tv station in province'),
            'gtw': ('卫星电视台', 'satellite tv station'),
        }),
        'gw': ('网络媒体', 'website', {
            'gwah': ('安徽网站', 'website about anhui'),
            'gwbj': ('北京网站', 'website about beijin'),
            'gwcj': ('财经网站', 'website about finance'),
            'gwcq': ('重庆网站', 'website about chongqing'),
            'gwdb': ('东北网站', 'website about northeast'),
            'gwdc': ('地产网站', 'website about estate'),
            'gwfj': ('福建网站', 'website about fujian'),
            'gwgd': ('广东网站', 'website about guangdong'),
            'gwgs': ('甘肃网站', 'website about gansu'),
            'gwgx': ('广西网站', 'website about guangxi'),
            'gwhan': ('海南网站', 'website about hainan'),
            'gwheb': ('河北网站', 'website about hebei'),
            'gwhen': ('河南网站', 'website about henan'),
            'gwhl': ('黑龙江网站', 'website about heilongjiang'),
            'gwhub': ('湖北网站', 'website about hubei'),
            'gwhun': ('湖南网站', 'website about hunan'),
            'gwit': ('IT网站', 'website about IT'),
            'gwjd': ('家电网站', 'website about appliances'),
            'gwjj': ('家居网站', 'website about home'),
            'gwjk': ('健康网站', 'website about health'),
            'gwjs': ('江苏网站', 'website about jiangsu'),
            'gwjx': ('江西网站', 'website about jiangxi'),
            'gwnm': ('内蒙古网站', 'website about neimenggu'),
            'gwot': ('其它网站', 'website about other'),
            'gwqc': ('汽车网站', 'website about car'),
            'gwqh': ('青海网站', 'website about qinhai'),
            'gwqz': ('亲子网站', 'website about child'),
            'gwsa': ('陕西网站', 'website about shan3xi'),
            'gwsc': ('四川网站', 'website about sichuan'),
            'gwsh': ('上海网站', 'website about shanghai'),
            'gwss': ('时尚网站', 'website about style'),
            'gwsx': ('山西网站', 'website about shanxi'),
            'gwsz': ('深圳网站', 'website about shenzhen'),
            'gwtj': ('天津网站', 'website about tianjin'),
            'gwxj': ('新疆网站', 'website about xinjiang'),
            'gwyn': ('云南网站', 'website about yunnan'),
            'gwz': ('全国网站', 'website about china'),
            'gwzj': ('浙江网站', 'website about zhejiang'),
        }),
    }),        
}


def _get_pos_name(pos_code, names='parent', english=True, pos_map=POS_MAP):
    """Gets the part of speech name for *pos_code*."""
    pos_code = pos_code.lower()  # Issue #10
    if names not in ('parent', 'child', 'all'):
        raise ValueError("names must be one of 'parent', 'child', or "
                         "'all'; not '{}'".format(names))
    logger.debug("Getting {} POS name for '{}' formatted as '{}'.".format(
                 'English' if english else 'Chinese', pos_code, names))
    for i in range(1, len(pos_code) + 1):
        try:
            pos_key = pos_code[0:i]
            pos_entry = pos_map[pos_key]
            break
        except KeyError:
            if i == len(pos_code):
                logger.warning("part of speech not recognized: '{}'".format(
                               pos_code))
                return None  # Issue #20
    pos = (pos_entry[1 if english else 0], )
    if names == 'parent':
        logger.debug("Part of speech name found: '{}'".format(pos[0]))
        return pos[0]
    if len(pos_entry) == 3 and pos_key != pos_code:
        sub_map = pos_entry[2]
        logger.debug("Found parent part of speech name '{}'. Descending to "
                     "look for child name for '{}'".format(
                         pos_entry[1], pos_code))
        sub_pos = _get_pos_name(pos_code, names, english, sub_map)

        if names == 'all':
            # sub_pos can be None sometimes (e.g. for a word '甲')
            pos = pos + sub_pos if sub_pos else pos
        else:
            pos = (sub_pos, )

    name = pos if names == 'all' else pos[-1]
    logger.debug("Part of speech name found: '{}'".format(name))
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
