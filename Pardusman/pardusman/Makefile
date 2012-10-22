all:
	pykdeuic4 -o gui/ui/main.py gui/ui/main.ui
	pykdeuic4 -o gui/ui/languages.py gui/ui/rawlanguages.ui
	pykdeuic4 -o gui/ui/packages.py gui/ui/packages.ui
	pykdeuic4 -o gui/ui/packagecollection.py gui/ui/packagecollection.ui
	pykdeuic4 -o gui/ui/raw_rc.py gui/ui/raw.qrc

clean:
	find -name *.pyc | xargs rm -rf
	rm -rf gui/ui/main.py
	rm -rf gui/ui/languages.py
	rm -rf gui/ui/packages.py
	rm -rf gui/ui/packagecollections.py
