#!/user/bin/env python
import re
from os.path import basename

class Base: #{

	def __init__(self):#{
		self.string = "This is a string. Isn't it? It is, right?";
		print(self.string.count("is"));
	#}
	
	def __fileNameCountStringLength__(): #{
		fileName = "MP_SN_1234567_pain.008.001.03_pain.008.001.03.sct_011111_141006121212";
		l = len(fileName);
		print(l);
	#}
	
	def __fileNameStringExtraction__(): #{
		fileName = "MP_SN_1234567_pain.008.001.03_pain.008.001.03.sct_011111_141006121212";
		first = re.search('SN_(.+?)_', fileName);
		second = re.search('sct_(.+?)_', fileName);
		print(first);
		print(second);
	#}
	
	def __fileNameStringExtraction2__(): #{
		fileName = "MP_SN_1234567_pain.008.001.03_pain.008.001.03.sct_011111_141006121212";
		start = fileName.index('SN_');
		end = fileName.find(start, );
		sub = fileName[start: end];
		print(sub);
	#}
	
	def __fileNameWithoutExtension__(): #{
		path = "a/b/c.txt";
		print(basename(path));
	#}
	
	def __extractTwoStringsIdsFromFileName__():#{
		path = "a/b/c/MP_SN_1234567_pain.008.001.03_pain.008.001.03.sct_011111_141006121212";
		fileName = basename(path);
		
		firstPositionForFirstString = fileName.find('SN_')+3;
		secondPositionForFirstString = fileName.find('_', firstPositionForFirstString);
		firstString = fileName[firstPositionForFirstString:secondPositionForFirstString];
		
		firstPositionForSecondString = fileName.find('sct_')+4;
		secondPositionForSecondString = fileName.find('_', firstPositionForSecondString);
		secondString = fileName[firstPositionForSecondString:secondPositionForSecondString];
		
		bothStrings = {'First String: ':firstString, 'Second String: ': secondString};
		
		print(bothStrings);
	#}
	
	def __extractTwoStringsIdsFromFileName2__(path):#{
		fileName = basename(path);
		
		firstPositionForFirstString = fileName.find('SN_')+3;
		secondPositionForFirstString = fileName.find('_', firstPositionForFirstString);
		firstString = fileName[firstPositionForFirstString:secondPositionForFirstString];
		
		firstPositionForSecondString = fileName.find('sct_')+4;
		secondPositionForSecondString = fileName.find('_', firstPositionForSecondString);
		secondString = fileName[firstPositionForSecondString:secondPositionForSecondString];
		
		bothStrings = {'First String: ':firstString, 'Second String: ': secondString};
		
		print(bothStrings);
	#}
	
	def __extractTwoStringsIdsFromFileName3__(): #{
		path = "a/b/c/MP_SN_1234567_pain.008.001.03_pain.008.001.03.sct_011111_141006121212";
		fileName = basename(path);
		
		firstString = re.search('SN_(.+?)_', fileName);
		#firstPartString = firstString[2:-1];
		
		secondString = re.search('sct_(.+?)_', fileName);
		#secondPartString = secondString[3:-1];
		
		#extractedStrings = {'First String: ': firstString[2:-1], 'Second String: ': secondString[3:-1]};
		extractedStrings = {'First String: ': firstString, 'Second String: ': secondString};
		
		print(firstString);
		print(secondString);
		#print(extractedStrings)
	#}
	
#}

myObject = Base();
path = "a/b/c/MP_SN_1234567_pain.008.001.03_pain.008.001.03.sct_011111_141006121212";
Base.__fileNameStringExtraction__();
Base.__fileNameWithoutExtension__();
Base.__extractTwoStringsIdsFromFileName__();
Base.__extractTwoStringsIdsFromFileName2__(path)
Base.__extractTwoStringsIdsFromFileName3__();

if(__name__ == "__main__"): #{
	root = Base();
#}



	
