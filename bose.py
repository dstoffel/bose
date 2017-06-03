# -*- coding: utf-8 -*-
from automation import *
import bosel
Rule = automation.Rule
rules = [
	Rule(id='action',pattern='joue la selection', out='laquel ?', childs=[
		Rule(id='preset', pattern='\d+', out='dans quel pièce', childs=[
			Rule(id='where', pattern='salon', out='salon'),
			Rule(id='where', pattern='bureau', out='bureau'),
		])
	]),
	Rule(id='action',pattern='joue la musique', out='dans quel pièce?', childs=[
			Rule(id='where', pattern='salon', out='salon'),
			Rule(id='where', pattern='bureau', out='bureau'),
	]),
	Rule(id='action',pattern='stop la musique', out='dans quel pièce?', childs=[
			Rule(id='where', pattern='salon', out='salon'),
			Rule(id='where', pattern='bureau', out='bureau'),
	])
]

class bose(automation):
	def __init__(self):
		super(bose, self).__init__()
		for rule in rules:
			self.register_rule(rule)
	def callback(self, data, m, rdata):
		if data['action'] == 'joue la selection':
			self.debug('playing %s in %s' % (data['preset'], data['where']))
			bosel.sendkey(data['where'], 'PRESET_%s' % data['preset'])
			bosel.sendkey(data['where'], 'PLAY')
		elif data['action'] == 'joue la musique':
			self.debug('playing musique %s' % data['where'])
			bosel.sendkey(data['where'], 'PLAY')
		elif data['action'] == 'stop la musique':
			self.debug('stoping musique %s' % data['where'])
			bosel.sendkey(data['where'], 'PAUSE')
		else:
			pass
		return "c'est fait"

