# split the text file
# address carrage returns
# remove punctuation?
# create a dict from individual words


# -*- coding: utf-8 -*-
import pytest

TEST_TEXT = [
    ('from', 'a', 'journey'),
    ('which', 'must', 'always'),
    ('he', 'was', 'employing'),
    ('pass', 'twice', 'in'),
    ('had', 'risen', 'out'),
    ('rang', 'the', 'bell')
]

SPLIT_TEXT = ['one', 'night', 'it', 'was', 'on', 'the', 'twentieth', 'of', 'march', '1888', 'i', 'was', 'returning', 'from', 'a', 'journey', 'to', 'a', 'patient', 'for', 'i', 'had', 'now', 'returned', 'to', 'civil', 'practice', 'when', 'my', 'way', 'led', 'me', 'through', 'baker', 'street', 'as', 'i', 'passed', 'the', 'well', 'remembered', 'door', 'which', 'must', 'always', 'be', 'associated', 'in', 'my', 'mind', 'with', 'my', 'wooing', 'and', 'with', 'the', 'dark', 'incidents', 'of', 'the', 'study', 'in', 'scarlet', 'i', 'was', 'seized', 'with', 'a', 'keen', 'desire', 'to', 'see', 'holmes', 'again', 'and', 'to', 'know', 'how', 'he', 'was', 'employing', 'his', 'extraordinary', 'powers', 'his', 'rooms', 'were', 'brilliantly', 'lit', 'and', 'even', 'as', 'i', 'looked', 'up', 'i', 'saw', 'his', 'tall', 'spare', 'figure', 'pass', 'twice', 'in', 'a', 'dark', 'silhouette', 'against', 'the', 'blind', 'he', 'was', 'pacing', 'the', 'room', 'swiftly', 'eagerly', 'with', 'his', 'head', 'sunk', 'upon', 'his', 'chest', 'and', 'his', 'hands', 'clasped', 'behind', 'him', 'to', 'me', 'who', 'knew', 'his', 'every', 'mood', 'and', 'habit', 'his', 'attitude', 'and', 'manner', 'told', 'their', 'own', 'story', 'he', 'was', 'at', 'work', 'again', 'he', 'had', 'risen', 'out', 'of', 'his', 'drug', 'created', 'dreams', 'and', 'was', 'hot', 'upon', 'the', 'scent', 'of', 'some', 'new', 'problem', 'i', 'rang', 'the', 'bell', 'and', 'was', 'shown', 'up', 'to', 'the', 'chamber', 'which', 'had', 'formerly', 'been', 'in', 'part', 'my', 'own']


TEXT_DICT = {('twice', 'in'): ['a'], ('with', 'the'): ['dark'], ('his', 'extraordinary'): ['powers'], ('and', 'to'): ['know'], ('through', 'baker'): ['street'], ('dark', 'silhouette'): ['against'], ('eagerly', 'with'): ['his'], ('for', 'i'): ['had'], ('associated', 'in'): ['my'], ('was', 'at'): ['work'], ('was', 'pacing'): ['the'], ('shown', 'up'): ['to'], ('was', 'employing'): ['his'], ('his', 'drug'): ['created'], ('me', 'who'): ['knew'], ('created', 'dreams'): ['and'], ('bell', 'and'): ['was'], ('a', 'keen'): ['desire'], ('with', 'his'): ['head'], ('sunk', 'upon'): ['his'], ('his', 'tall'): ['spare'], ('tall', 'spare'): ['figure'], ('up', 'to'): ['the'], ('was', 'returning'): ['from'], ('rooms', 'were'): ['brilliantly'], ('the', 'chamber'): ['which'], ('in', 'part'): ['my'], ('pacing', 'the'): ['room'], ('head', 'sunk'): ['upon'], ('his', 'hands'): ['clasped'], ('returned', 'to'): ['civil'], ('in', 'a'): ['dark'], ('of', 'his'): ['drug'], ('upon', 'his'): ['chest'], ('and', 'his'): ['hands'], ('had', 'formerly'): ['been'], ('him', 'to'): ['me'], ('problem', 'i'): ['rang'], ('part', 'my'): ['own'], ('against', 'the'): ['blind'], ('journey', 'to'): ['a'], ('looked', 'up'): ['i'], ('mood', 'and'): ['habit'], ('wooing', 'and'): ['with'], ('swiftly', 'eagerly'): ['with'], ('to', 'the'): ['chamber'], ('study', 'in'): ['scarlet'], ('the', 'bell'): ['and'], ('pass', 'twice'): ['in'], ('his', 'chest'): ['and'], ('up', 'i'): ['saw'], ('to', 'know'): ['how'], ('their', 'own'): ['story'], ('and', 'with'): ['the'], ('baker', 'street'): ['as'], ('a', 'journey'): ['to'], ('was', 'shown'): ['up'], ('i', 'passed'): ['the'], ('the', 'scent'): ['of'], ('door', 'which'): ['must'], ('room', 'swiftly'): ['eagerly'], ('incidents', 'of'): ['the'], ('chest', 'and'): ['his'], ('and', 'habit'): ['his'], ('the', 'study'): ['in'], ('scarlet', 'i'): ['was'], ('figure', 'pass'): ['twice'], ('work', 'again'): ['he'], ('even', 'as'): ['i'], ('keen', 'desire'): ['to'], ('his', 'rooms'): ['were'], ('manner', 'told'): ['their'], ('employing', 'his'): ['extraordinary'], ('out', 'of'): ['his'], ('i', 'was'): ['returning', 'seized'], ('again', 'and'): ['to'], ('a', 'patient'): ['for'], ('always', 'be'): ['associated'], ('he', 'had'): ['risen'], ('some', 'new'): ['problem'], ('behind', 'him'): ['to'], ('had', 'now'): ['returned'], ('see', 'holmes'): ['again'], ('rang', 'the'): ['bell'], ('of', 'the'): ['study'], ('extraordinary', 'powers'): ['his'], ('to', 'civil'): ['practice'], ('was', 'hot'): ['upon'], ('his', 'attitude'): ['and'], ('he', 'was'): ['employing', 'pacing', 'at'], ('drug', 'created'): ['dreams'], ('own', 'story'): ['he'], ('must', 'always'): ['be'], ('in', 'my'): ['mind'], ('of', 'some'): ['new'], ('to', 'see'): ['holmes'], ('my', 'wooing'): ['and'], ('mind', 'with'): ['my'], ('and', 'was'): ['hot', 'shown'], ('was', 'on'): ['the'], ('now', 'returned'): ['to'], ('were', 'brilliantly'): ['lit'], ('habit', 'his'): ['attitude'], ('the', 'blind'): ['he'], ('led', 'me'): ['through'], ('hands', 'clasped'): ['behind'], ('lit', 'and'): ['even'], ('i', 'saw'): ['his'], ('me', 'through'): ['baker'], ('his', 'every'): ['mood'], ('which', 'must'): ['always'], ('again', 'he'): ['had'], ('a', 'dark'): ['silhouette'], ('who', 'knew'): ['his'], ('clasped', 'behind'): ['him'], ('chamber', 'which'): ['had'], ('new', 'problem'): ['i'], ('silhouette', 'against'): ['the'], ('with', 'a'): ['keen'], ('of', 'march'): ['1888'], ('at', 'work'): ['again'], ('as', 'i'): ['passed', 'looked'], ('to', 'me'): ['who'], ('i', 'looked'): ['up'], ('march', '1888'): ['i'], ('formerly', 'been'): ['in'], ('spare', 'figure'): ['pass'], ('twentieth', 'of'): ['march'], ('remembered', 'door'): ['which'], ('to', 'a'): ['patient'], ('street', 'as'): ['i'], ('dreams', 'and'): ['was'], ('how', 'he'): ['was'], ('returning', 'from'): ['a'], ('been', 'in'): ['part'], ('1888', 'i'): ['was'], ('night', 'it'): ['was'], ('i', 'rang'): ['the'], ('the', 'well'): ['remembered'], ('from', 'a'): ['journey'], ('when', 'my'): ['way'], ('one', 'night'): ['it'], ('know', 'how'): ['he'], ('practice', 'when'): ['my'], ('hot', 'upon'): ['the'], ('desire', 'to'): ['see'], ('i', 'had'): ['now'], ('story', 'he'): ['was'], ('brilliantly', 'lit'): ['and'], ('the', 'room'): ['swiftly'], ('the', 'twentieth'): ['of'], ('blind', 'he'): ['was'], ('the', 'dark'): ['incidents'], ('risen', 'out'): ['of'], ('and', 'even'): ['as'], ('powers', 'his'): ['rooms'], ('my', 'way'): ['led'], ('civil', 'practice'): ['when'], ('saw', 'his'): ['tall'], ('every', 'mood'): ['and'], ('knew', 'his'): ['every'], ('attitude', 'and'): ['manner'], ('patient', 'for'): ['i'], ('way', 'led'): ['me'], ('told', 'their'): ['own'], ('had', 'risen'): ['out'], ('be', 'associated'): ['in'], ('passed', 'the'): ['well'], ('my', 'mind'): ['with'], ('it', 'was'): ['on'], ('upon', 'the'): ['scent'], ('seized', 'with'): ['a'], ('was', 'seized'): ['with'], ('which', 'had'): ['formerly'], ('on', 'the'): ['twentieth'], ('holmes', 'again'): ['and'], ('well', 'remembered'): ['door'], ('in', 'scarlet'): ['i'], ('his', 'head'): ['sunk'], ('and', 'manner'): ['told'], ('scent', 'of'): ['some'], ('dark', 'incidents'): ['of'], ('with', 'my'): ['wooing']}

TEXT_DICT_SMALL = {('with', 'my'): ['wooing']}


def test_file_load():
    from trigrams import file_load
    assert file_load('sherlock_small.txt') == SPLIT_TEXT


def test_make_dict():
    from trigrams import make_dict
    assert make_dict(SPLIT_TEXT) == TEXT_DICT

def test_build_output():
    from trigrams import build_output
    assert build_output(TEXT_DICT_SMALL, 1) == ['with', 'my', 'wooing']


def test_choose_next():
    from trigrams import choose_next
    assert choose_next(('with', 'my'), TEXT_DICT_SMALL) == ('my', 'wooing')
