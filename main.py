from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtCore import Qt
from sys import argv, exit
from math import sqrt
from random import choices
icons = {'ti-wand': '\ue600', 'ti-volume': '\ue601', 'ti-user': '\ue602', 'ti-unlock': '\ue603', 'ti-unlink': '\ue604', 'ti-trash': '\ue605', 'ti-thought': '\ue606', 'ti-target': '\ue607', 'ti-tag': '\ue608', 'ti-tablet': '\ue609', 'ti-star': '\ue60a', 'ti-spray': '\ue60b', 'ti-signal': '\ue60c', 'ti-shopping-cart': '\ue60d', 'ti-shopping-cart-full': '\ue60e', 'ti-settings': '\ue60f', 'ti-search': '\ue610', 'ti-zoom-in': '\ue611', 'ti-zoom-out': '\ue612', 'ti-cut': '\ue613', 'ti-ruler': '\ue614', 'ti-ruler-pencil': '\ue615', 'ti-ruler-alt': '\ue616', 'ti-bookmark': '\ue617', 'ti-bookmark-alt': '\ue618', 'ti-reload': '\ue619', 'ti-plus': '\ue61a', 'ti-pin': '\ue61b', 'ti-pencil': '\ue61c', 'ti-pencil-alt': '\ue61d', 'ti-paint-roller': '\ue61e', 'ti-paint-bucket': '\ue61f', 'ti-na': '\ue620', 'ti-mobile': '\ue621', 'ti-minus': '\ue622', 'ti-medall': '\ue623', 'ti-medall-alt': '\ue624', 'ti-marker': '\ue625', 'ti-marker-alt': '\ue626', 'ti-arrow-up': '\ue627', 'ti-arrow-right': '\ue628', 'ti-arrow-left': '\ue629', 'ti-arrow-down': '\ue62a', 'ti-lock': '\ue62b', 'ti-location-arrow': '\ue62c', 'ti-link': '\ue62d', 'ti-layout': '\ue62e', 'ti-layers': '\ue62f', 'ti-layers-alt': '\ue630', 'ti-key': '\ue631', 'ti-import': '\ue632', 'ti-image': '\ue633', 'ti-heart': '\ue634', 'ti-heart-broken': '\ue635', 'ti-hand-stop': '\ue636', 'ti-hand-open': '\ue637', 'ti-hand-drag': '\ue638', 'ti-folder': '\ue639', 'ti-flag': '\ue63a', 'ti-flag-alt': '\ue63b', 'ti-flag-alt-2': '\ue63c', 'ti-eye': '\ue63d', 'ti-export': '\ue63e', 'ti-exchange-vertical': '\ue63f', 'ti-desktop': '\ue640', 'ti-cup': '\ue641', 'ti-crown': '\ue642', 'ti-comments': '\ue643', 'ti-comment': '\ue644', 'ti-comment-alt': '\ue645', 'ti-close': '\ue646', 'ti-clip': '\ue647', 'ti-angle-up': '\ue648', 'ti-angle-right': '\ue649', 'ti-angle-left': '\ue64a', 'ti-angle-down': '\ue64b', 'ti-check': '\ue64c', 'ti-check-box': '\ue64d', 'ti-camera': '\ue64e', 'ti-announcement': '\ue64f', 'ti-brush': '\ue650', 'ti-briefcase': '\ue651', 'ti-bolt': '\ue652', 'ti-bolt-alt': '\ue653', 'ti-blackboard': '\ue654', 'ti-bag': '\ue655', 'ti-move': '\ue656', 'ti-arrows-vertical': '\ue657', 'ti-arrows-horizontal': '\ue658', 'ti-fullscreen': '\ue659', 'ti-arrow-top-right': '\ue65a', 'ti-arrow-top-left': '\ue65b', 'ti-arrow-circle-up': '\ue65c', 'ti-arrow-circle-right': '\ue65d', 'ti-arrow-circle-left': '\ue65e', 'ti-arrow-circle-down': '\ue65f', 'ti-angle-double-up': '\ue660', 'ti-angle-double-right': '\ue661', 'ti-angle-double-left': '\ue662', 'ti-angle-double-down': '\ue663', 'ti-zip': '\ue664', 'ti-world': '\ue665', 'ti-wheelchair': '\ue666', 'ti-view-list': '\ue667', 'ti-view-list-alt': '\ue668', 'ti-view-grid': '\ue669', 'ti-uppercase': '\ue66a', 'ti-upload': '\ue66b', 'ti-underline': '\ue66c', 'ti-truck': '\ue66d', 'ti-timer': '\ue66e', 'ti-ticket': '\ue66f', 'ti-thumb-up': '\ue670', 'ti-thumb-down': '\ue671', 'ti-text': '\ue672', 'ti-stats-up': '\ue673', 'ti-stats-down': '\ue674', 'ti-split-v': '\ue675', 'ti-split-h': '\ue676', 'ti-smallcap': '\ue677', 'ti-shine': '\ue678', 'ti-shift-right': '\ue679', 'ti-shift-left': '\ue67a', 'ti-shield': '\ue67b', 'ti-notepad': '\ue67c', 'ti-server': '\ue67d', 'ti-quote-right': '\ue67e', 'ti-quote-left': '\ue67f', 'ti-pulse': '\ue680', 'ti-printer': '\ue681', 'ti-power-off': '\ue682', 'ti-plug': '\ue683', 'ti-pie-chart': '\ue684', 'ti-paragraph': '\ue685', 'ti-panel': '\ue686', 'ti-package': '\ue687', 'ti-music': '\ue688', 'ti-music-alt': '\ue689', 'ti-mouse': '\ue68a', 'ti-mouse-alt': '\ue68b', 'ti-money': '\ue68c', 'ti-microphone': '\ue68d', 'ti-menu': '\ue68e', 'ti-menu-alt': '\ue68f', 'ti-map': '\ue690', 'ti-map-alt': '\ue691', 'ti-loop': '\ue692', 'ti-location-pin': '\ue693', 'ti-list': '\ue694', 'ti-light-bulb': '\ue695', 'ti-Italic': '\ue696', 'ti-info': '\ue697', 'ti-infinite': '\ue698', 'ti-id-badge': '\ue699', 'ti-hummer': '\ue69a', 'ti-home': '\ue69b', 'ti-help': '\ue69c', 'ti-headphone': '\ue69d', 'ti-harddrives': '\ue69e', 'ti-harddrive': '\ue69f', 'ti-gift': '\ue6a0', 'ti-game': '\ue6a1', 'ti-filter': '\ue6a2', 'ti-files': '\ue6a3', 'ti-file': '\ue6a4', 'ti-eraser': '\ue6a5', 'ti-envelope': '\ue6a6', 'ti-download': '\ue6a7', 'ti-direction': '\ue6a8', 'ti-direction-alt': '\ue6a9', 'ti-dashboard': '\ue6aa', 'ti-control-stop': '\ue6ab', 'ti-control-shuffle': '\ue6ac', 'ti-control-play': '\ue6ad', 'ti-control-pause': '\ue6ae', 'ti-control-forward': '\ue6af', 'ti-control-backward': '\ue6b0', 'ti-cloud': '\ue6b1', 'ti-cloud-up': '\ue6b2', 'ti-cloud-down': '\ue6b3', 'ti-clipboard': '\ue6b4', 'ti-car': '\ue6b5', 'ti-calendar': '\ue6b6', 'ti-book': '\ue6b7', 'ti-bell': '\ue6b8', 'ti-basketball': '\ue6b9', 'ti-bar-chart': '\ue6ba', 'ti-bar-chart-alt': '\ue6bb', 'ti-back-right': '\ue6bc', 'ti-back-left': '\ue6bd', 'ti-arrows-corner': '\ue6be', 'ti-archive': '\ue6bf', 'ti-anchor': '\ue6c0', 'ti-align-right': '\ue6c1', 'ti-align-left': '\ue6c2', 'ti-align-justify': '\ue6c3', 'ti-align-center': '\ue6c4', 'ti-alert': '\ue6c5', 'ti-alarm-clock': '\ue6c6', 'ti-agenda': '\ue6c7', 'ti-write': '\ue6c8', 'ti-window': '\ue6c9', 'ti-widgetized': '\ue6ca', 'ti-widget': '\ue6cb', 'ti-widget-alt': '\ue6cc', 'ti-wallet': '\ue6cd', 'ti-video-clapper': '\ue6ce', 'ti-video-camera': '\ue6cf', 'ti-vector': '\ue6d0', 'ti-themify-logo': '\ue6d1', 'ti-themify-favicon': '\ue6d2', 'ti-themify-favicon-alt': '\ue6d3', 'ti-support': '\ue6d4', 'ti-stamp': '\ue6d5', 'ti-split-v-alt': '\ue6d6', 'ti-slice': '\ue6d7', 'ti-shortcode': '\ue6d8', 'ti-shift-right-alt': '\ue6d9', 'ti-shift-left-alt': '\ue6da', 'ti-ruler-alt-2': '\ue6db', 'ti-receipt': '\ue6dc', 'ti-pin2': '\ue6dd', 'ti-pin-alt': '\ue6de', 'ti-pencil-alt2': '\ue6df', 'ti-palette': '\ue6e0', 'ti-more': '\ue6e1', 'ti-more-alt': '\ue6e2', 'ti-microphone-alt': '\ue6e3', 'ti-magnet': '\ue6e4', 'ti-line-double': '\ue6e5', 'ti-line-dotted': '\ue6e6', 'ti-line-dashed': '\ue6e7', 'ti-layout-width-full': '\ue6e8', 'ti-layout-width-default': '\ue6e9', 'ti-layout-width-default-alt': '\ue6ea', 'ti-layout-tab': '\ue6eb', 'ti-layout-tab-window': '\ue6ec', 'ti-layout-tab-v': '\ue6ed', 'ti-layout-tab-min': '\ue6ee', 'ti-layout-slider': '\ue6ef', 'ti-layout-slider-alt': '\ue6f0', 'ti-layout-sidebar-right': '\ue6f1', 'ti-layout-sidebar-none': '\ue6f2', 'ti-layout-sidebar-left': '\ue6f3', 'ti-layout-placeholder': '\ue6f4', 'ti-layout-menu': '\ue6f5', 'ti-layout-menu-v': '\ue6f6', 'ti-layout-menu-separated': '\ue6f7', 'ti-layout-menu-full': '\ue6f8', 'ti-layout-media-right-alt': '\ue6f9', 'ti-layout-media-right': '\ue6fa', 'ti-layout-media-overlay': '\ue6fb', 'ti-layout-media-overlay-alt': '\ue6fc', 'ti-layout-media-overlay-alt-2': '\ue6fd', 'ti-layout-media-left-alt': '\ue6fe', 'ti-layout-media-left': '\ue6ff', 'ti-layout-media-center-alt': '\ue700', 'ti-layout-media-center': '\ue701', 'ti-layout-list-thumb': '\ue702', 'ti-layout-list-thumb-alt': '\ue703', 'ti-layout-list-post': '\ue704', 'ti-layout-list-large-image': '\ue705', 'ti-layout-line-solid': '\ue706', 'ti-layout-grid4': '\ue707', 'ti-layout-grid3': '\ue708', 'ti-layout-grid2': '\ue709', 'ti-layout-grid2-thumb': '\ue70a', 'ti-layout-cta-right': '\ue70b', 'ti-layout-cta-left': '\ue70c', 'ti-layout-cta-center': '\ue70d', 'ti-layout-cta-btn-right': '\ue70e', 'ti-layout-cta-btn-left': '\ue70f', 'ti-layout-column4': '\ue710', 'ti-layout-column3': '\ue711', 'ti-layout-column2': '\ue712', 'ti-layout-accordion-separated': '\ue713', 'ti-layout-accordion-merged': '\ue714', 'ti-layout-accordion-list': '\ue715', 'ti-ink-pen': '\ue716', 'ti-info-alt': '\ue717', 'ti-help-alt': '\ue718', 'ti-headphone-alt': '\ue719', 'ti-hand-point-up': '\ue71a', 'ti-hand-point-right': '\ue71b', 'ti-hand-point-left': '\ue71c', 'ti-hand-point-down': '\ue71d', 'ti-gallery': '\ue71e', 'ti-face-smile': '\ue71f', 'ti-face-sad': '\ue720', 'ti-credit-card': '\ue721', 'ti-control-skip-forward': '\ue722', 'ti-control-skip-backward': '\ue723', 'ti-control-record': '\ue724', 'ti-control-eject': '\ue725', 'ti-comments-smiley': '\ue726', 'ti-brush-alt': '\ue727', 'ti-youtube': '\ue728', 'ti-vimeo': '\ue729', 'ti-twitter': '\ue72a', 'ti-time': '\ue72b', 'ti-tumblr': '\ue72c', 'ti-skype': '\ue72d', 'ti-share': '\ue72e', 'ti-share-alt': '\ue72f', 'ti-rocket': '\ue730', 'ti-pinterest': '\ue731', 'ti-new-window': '\ue732', 'ti-microsoft': '\ue733', 'ti-list-ol': '\ue734', 'ti-linkedin': '\ue735', 'ti-layout-sidebar-2': '\ue736', 'ti-layout-grid4-alt': '\ue737', 'ti-layout-grid3-alt': '\ue738', 'ti-layout-grid2-alt': '\ue739', 'ti-layout-column4-alt': '\ue73a', 'ti-layout-column3-alt': '\ue73b', 'ti-layout-column2-alt': '\ue73c', 'ti-instagram': '\ue73d', 'ti-google': '\ue73e', 'ti-github': '\ue73f', 'ti-flickr': '\ue740', 'ti-facebook': '\ue741', 'ti-dropbox': '\ue742', 'ti-dribbble': '\ue743', 'ti-apple': '\ue744', 'ti-android': '\ue745', 'ti-save': '\ue746', 'ti-save-alt': '\ue747', 'ti-yahoo': '\ue748', 'ti-wordpress': '\ue749', 'ti-vimeo-alt': '\ue74a', 'ti-twitter-alt': '\ue74b', 'ti-tumblr-alt': '\ue74c', 'ti-trello': '\ue74d', 'ti-stack-overflow': '\ue74e', 'ti-soundcloud': '\ue74f', 'ti-sharethis': '\ue750', 'ti-sharethis-alt': '\ue751', 'ti-reddit': '\ue752', 'ti-pinterest-alt': '\ue753', 'ti-microsoft-alt': '\ue754', 'ti-linux': '\ue755', 'ti-jsfiddle': '\ue756', 'ti-joomla': '\ue757', 'ti-html5': '\ue758', 'ti-flickr-alt': '\ue759', 'ti-email': '\ue75a', 'ti-drupal': '\ue75b', 'ti-dropbox-alt': '\ue75c', 'ti-css3': '\ue75d', 'ti-rss': '\ue75e', 'ti-rss-alt': '\ue75f'}
class Cell(QWidget):
	def __init__(self, p, *cos):
		super().__init__(p)
		self.x, self.y = cos
		self.marked, self.opened, self.bombed, self.checked = False, False, False, False
		self.setStyleSheet("border: 1px solid black")
		self.label = QLabel(self)
		self.label.setAlignment(Qt.AlignCenter)

	def check(self):
		c = 0
		index = self.y*int(sqrt(len(self.parent().grid)))+self.x
		if not self.checked:
			self.checked = True
			b1 = (self.y-1)*int(sqrt(len(self.parent().grid)))
			b2 = self.y*int(sqrt(len(self.parent().grid)))
			b3 = (self.y+1)*int(sqrt(len(self.parent().grid)))
			b4 = (self.y+2)*int(sqrt(len(self.parent().grid)))
			for i in [int(-sqrt(len(self.parent().grid)+1))-1, int(-sqrt(len(self.parent().grid)+1)), int(-sqrt(len(self.parent().grid)+1))+1]:
				if 0 <= b1 <= index+i < b2 < len(self.parent().grid) and self.parent().grid[index+i].bombed:
					c += 1
			for i in [-1, 1]:
				if 0 <= b2 <= index+i < b3 < len(self.parent().grid) and self.parent().grid[index+i].bombed:
					c += 1
			for i in [sqrt(len(self.parent().grid)+1)-1, sqrt(len(self.parent().grid)+1), sqrt(len(self.parent().grid)+1)+1]:
				if 0 <= b3 <= int(index+i) < b4 < len(self.parent().grid) and self.parent().grid[int(index+i)].bombed:
					c += 1
			print(self.x, self.y, c)
			self.label.setText(str(c))
			if c == 0:
				for i in [int(-sqrt(len(self.parent().grid)+1))-1, int(-sqrt(len(self.parent().grid)+1)), int(-sqrt(len(self.parent().grid)+1))+1]:
					if 0 <= b1 <= index+i < b2 < len(self.parent().grid):
						self.parent().grid[index+i].check()

				for i in [-1, 1]:
					if 0 <= b2 <= index+i < b3 < len(self.parent().grid):
						self.parent().grid[index+i].check()

				for i in [sqrt(len(self.parent().grid)+1)-1, sqrt(len(self.parent().grid)+1), sqrt(len(self.parent().grid)+1)+1]:
					if 0 <= b3 <= int(index+i) < b4 < len(self.parent().grid):
						self.parent().grid[int(index+i)].check()

	def mousePressEvent(self, e):
		if e.button() == Qt.LeftButton:
			if not self.opened:
				# self.opened = True
				if self.bombed:
					self.label.setText(icons["ti-target"])
				else:
					print("check")
					self.checked = False
					self.check()
					for c in self.parent().grid: c.checked = False
		elif e.button() == Qt.RightButton:
			if not self.opened:
				if not self.marked:
					self.label.setText(icons["ti-help"])
				else:
					self.label.setText("")
				self.marked = not self.marked
	def resizeEvent(self, e):
		self.label.setGeometry(0, 0, self.width(), self.height())
		self.label.setStyleSheet("font-size: " + str(min([self.width(), self.height()])) +"px;")

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setMinimumSize(400, 400)
		self.setStyleSheet(".Cell *, #Icon{font-family: themify;}")
		self.grid = [Cell(self, x, y) for y in range(5) for x in range(5)]
		for i in choices(self.grid, k=5):
			i.bombed = True
			i.label.setText(icons["ti-target"])
	def resizeEvent(self, e):
		w, h = int(self.width()/sqrt(len(self.grid))), int(self.height()/sqrt(len(self.grid)))
		for c in self.grid:
			c.setGeometry(c.x*w, c.y*h, w, h)




app = QApplication(argv)
QFontDatabase.addApplicationFont("icons.ttf")

mw = MainWindow()
mw.show()


exit(app.exec_())