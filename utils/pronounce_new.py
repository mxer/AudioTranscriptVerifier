# coding=utf-8
import Constants as cs
# import preprocessor as pp
# import IndicNormalizer as norm

class Stacked:
    def __init__(self):
        self.top = -1
        self.list = [None] * 500

    def push(self, push):
        self.top = self.top + 1
        self.list[self.top] = push

    def pop(self):
        # self.list[self.top]
        self.top = self.top - 1

    def get(self):
        temp = ""
        for i in range(0, self.top + 1):
            if i != self.top:
                temp += self.list[i]
                if temp[-1] != ' ':
                    temp += " "
            else:
                temp += self.list[i]
                temp = temp.strip()
                tlist = temp.split()
                for c in tlist:
                    if c == "":
                        print("Blank")
                        print(temp)
        return temp


class Mappings:
    prevState = -1
    stateConsonant = 0
    stateVowel = 1
    stateMatra = 2

    stack = Stacked()

    def __init__(self):
        self.stack = Stacked()

    phone_map = [

        {
            u"\u0900": u"N",  # inverted chandrabindu
            u"\u0901" : u"N",				# chandrabindu
            u"\u0902"	: u"N",					# anuswar
            u"\u0903"	: u"HH",			# visarga
            u"\u0904"	: u"EY",				# ऄ
            u"\u0905"	: u"AH",				# अ
            u"\u0906"	: u"AA",				# आ
            u"\u0907"	: u"IH",				# इ
            u"\u0908"	: u"IY",				# ई
            u"\u0909"	: u"UH",				# उ
            u"\u090A"	: u"UW",				# ऊ
            u"\u090B"	: u"R IH",				# ऋ
            u"\u090C"	: u"L R IH",			# ऌ
            u"\u090D"	: u"AE",				# ऍ
            u"\u090E"	: u"EY",				# ऎ
            u"\u090F"	: u"EY",				# ए
            u"\u0910"	: u"AE",				# ऐ
            u"\u0911"	: u"AO",				# ऑ
            u"\u0912"	: u"OW",				# ऒ
            u"\u0913"	: u"OW",				# ओ
            u"\u0914"	: u"AO",				# औ
            u"\u0915"	: u"K",					# क
            u"\u0916"	: u"KH",				# ख
            u"\u0917"	: u"G",					# ग
            u"\u0918"	: u"GH",				# घ
            u"\u0919"	: u"N",					# ङ
            u"\u091A"	: u"CH",				# च
            u"\u091B"	: u"CHH",				# छ
            u"\u091C"	: u"JH",				# ज
            u"\u091D"	: u"JHH",				# झ
            u"\u091E"	: u"N",					# ञ
            u"\u091F"	: u"TT",				# ट
            u"\u0920"	: u"TTH",				# ठ
            u"\u0921"	: u"DD",				# ड
            u"\u0922"	: u"DDH",				# ढ
            u"\u0923"	: u"NN",				# ण
            u"\u0924"	: u"T",					# त
            u"\u0925"	: u"TH",				# थ
            u"\u0926"	: u"D",					# द
            u"\u0927"	: u"DH",				# ध
            u"\u0928"	: u"N",					# न
            u"\u0929"	: u"N",					# ऩ
            u"\u092A"	: u"P",					# प
            u"\u092B"	: u"F",					# फ
            u"\u092C"	: u"B",					# ब
            u"\u092D"	: u"BH",				# भ
            u"\u092E"	: u"M",					# म
            u"\u092F"	: u"Y",					# य
            u"\u0930"	: u"R",					# र
            u"\u0931"	: u"R",					# ऱ
            u"\u0932"	: u"L",					# ल
            u"\u0933"	: u"L",					# ळ
            u"\u0934"	: u"L",					# ऴ
            u"\u0935"	: u"W",					# ‌व
            u"\u0936"	: u"SH",				# श
            u"\u0937"	: u"SH",				# ष
            u"\u0938"	: u"S",					# स
            u"\u0939"	: u"HH",				# ह
            u"\u093A"	: u"",					# ऺ
            u"\u093B"	: u"",					# ऻ
            u"\u093C"	: u"",					# nukta
            u"\u093D"	: u"AH",				# avagraha
            u"\u093E"	: u"AA",				# ऽ
            u"\u093F"	: u"IH",				# ि
            u"\u0940"	: u"IY",				# ी
            u"\u0941"	: u"UH",				# ु
            u"\u0942"	: u"UW",				# ू
            u"\u0943"	: u"R IH",				# ृ
            u"\u0944"	: u"",					# ॄ
            u"\u0945"	: u"AE",				# ॅ
            u"\u0946"	: u"EY",				# ॆ
            u"\u0947"	: u"EY",				# े
            u"\u0948"	: u"AE",				# ै
            u"\u0949"	: u"AO",				# ॉ
            u"\u094A"	: u"OW",				# ॊ
            u"\u094B"	: u"OW",				# ो
            u"\u094C"	: u"AO",				# ौ
            u"\u094D"	: u"",					# ्    - virama
            u"\u094E"	: u"",					# ॎ - pristhavirama
            u"\u094F"	: u"AO",				# ॏ
            u"\u0950"	: u"OW M",				# ॐ
            u"\u0951"	: u"",					# ◌॑
            u"\u0952"	: u"",					# ◌॒
            u"\u0953"	: u"",					# ॓॓
            u"\u0954"	: u"",					# ॔
            u"\u0955"	: u"",					# ॕ
            u"\u0956"	: u"",					# ॖ
            u"\u0957"	: u"",					# ॗ
            u"\u0958"	: u"K",					# क़
            u"\u0959"	: u"KH",				# ख़
            u"\u095A"	: u"G",					# ग़
            u"\u095B"	: u"JH",					# ज़
            u"\u095C"	: u"DD",				# ड़
            u"\u095D"	: u"DDH",				# ढ़
            u"\u095E"	: u"F",					# फ़
            u"\u095F"	: u"Y",					# य़
            u"\u0960"	: u"R IH",				# ॠ
            u"\u0961"	: u"L R IH",			# ॡ
            u":"		: u"",
            u"!"		: u"",
            u"'"		: u"",
            u"‘"		: u"",
            u"\u2019"	: u"",
            u"\u200C"	: u"",
            u"\u200D"	: u"",
            u'\u2013'	: u"",
            u'/'		: u"",
            u'['		: u"",
            u']'		: u"",
            u'*'		: u"",
            u'\u0964'	: u"",


        },
        # Gujarati
        {

        },
        # Punjabi
        {

        },
        # Malayalam
        {

        },
        # Tamil
        {

        },
        # Telugu
        {

        },
        # Kannada
        {

        },
        {
            # Odia
            u"\u0B01": "N",
            u"\u0B02": "N",
            u"\u0B03": "HH",
            u"\u0B05": "AH",
            u"\u0B06": "AA",
            u"\u0B07": "IH",
            u"\u0B08": "IY",
            u"\u0B09": "UH",
            u"\u0B0A": "UW",
            u"\u0B0B": "R IH",
            u"\u0B0C": "L R IH",  # Not sure
            u"\u0B0F": "EY",

            u"\u0B10": "OY",
            u"\u0B13": "AO",
            u"\u0B14": "OW",
            u"\u0B15": "K",
            u"\u0B16": "KH",
            u"\u0B17": "G",
            u"\u0B18": "GH",
            u"\u0B19": "N",
            u"\u0B1A": "CH",
            u"\u0B1B": "CHH",
            u"\u0B1C": "JH",
            u"\u0B1D": "JHH",
            u"\u0B1E": "N",
            u"\u0B1F": "TT",

            u"\u0B20": "TTH",
            u"\u0B21": "DD",
            u"\u0B22": "DDH",
            u"\u0B23": "NN",
            u"\u0B24": "T",
            u"\u0B25": "TH",
            u"\u0B26": "D",
            u"\u0B27": "DH",
            u"\u0B28": "N",
            u"\u0B2A": "P",
            u"\u0B2B": "F",
            u"\u0B2C": "B",
            u"\u0B2D": "BH",
            u"\u0B2E": "M",
            u"\u0B2F": "ZH",

            u"\u0B30": "R",
            u"\u0B32": "L",
            u"\u0B33": "L",  # Not Sure
            u"\u0B35": "W",
            u"\u0B36": "SH",
            u"\u0B37": "SH",
            u"\u0B38": "S",
            u"\u0B39": "HH",
            u"\u0B3E": "AA",
            u"\u0B3F": "IH",

            u"\u0B40": "IY",
            u"\u0B41": "UH",
            u"\u0B42": "UW",
            u"\u0B43": "R IH",
            u"\u0B47": "EY",
            u"\u0B48": "OY",
            u"\u0B4B": "AO",
            u"\u0B4C": "OW",
            u"\u0B4D": "",

            u"\u0B5C": "DD",
            u"\u0B5D": "DDH",
            u"\u0B5F": "Y",

            u"\u0B60": "R IH",
            u"\u0B71": "W",  # Not Sure

            u"\u02019": "",
            u"\u0200C": "",
            u"\u0200D": "",
            u"\u02013": "",
        },
        {
            # Bengali
            u"\u0981": "N",
            u"\u0982": "N",
            u"\u0983": "HH",
            u"\u0984": "",
            u"\u0985": "AH",
            u"\u0986": "AA",
            u"\u0987": "IH",
            u"\u0988": "IY",
            u"\u0989": "UH",
            u"\u098A": "UW",
            u"\u098B": "R IH",
            u"\u098C": "L R IH",
            u"\u098D": "",
            u"\u098E": "",
            u"\u098F": "AE",

            u"\u0990": "OY",
            u"\u0991": "",
            u"\u0992": "",
            u"\u0993": "AO",
            u"\u0994": "OW",
            u"\u0995": "K",
            u"\u0996": "KH",
            u"\u0997": "G",
            u"\u0998": "GH",
            u"\u0999": "N",
            u"\u099A": "SH",
            u"\u099B": "SH",
            u"\u099C": "JH",
            u"\u099D": "JHH",
            u"\u099E": "N",
            u"\u099F": "TT",

            u"\u09a0": "TTH",
            u"\u09a1": "DD",
            u"\u09a2": "DDH",
            u"\u09a3": "NN",
            u"\u09a4": "T",
            u"\u09a5": "TH",
            u"\u09a6": "D",
            u"\u09a7": "DH",
            u"\u09a8": "N",
            u"\u09aA": "P",
            u"\u09aB": "F",
            u"\u09aC": "B",
            u"\u09aD": "BH",
            u"\u09aE": "M",
            u"\u09aF": "ZH",

            u"\u09b0": "R",
            u"\u09b1": "",
            u"\u09b2": "L",
            u"\u09b3": "",
            u"\u09b4": "",
            u"\u09b5": "",
            u"\u09b6": "SH",
            u"\u09b7": "SH",
            u"\u09b8": "S",
            u"\u09b9": "HH",
            u"\u09bA": "",
            u"\u09BB": "",
            u"\u09BC": "",
            u"\u09bD": "AH",
            u"\u09bE": "AA",
            u"\u09bF": "IH",

            u"\u09c0": "IY",
            u"\u09c1": "UH",
            u"\u09c2": "UW",
            u"\u09c3": "R IH",
            u"\u09c4": "",
            u"\u09c5": "",
            u"\u09c6": "",
            u"\u09c7": "EY",
            u"\u09c8": "OY",
            u"\u09ca": "",
            u"\u09cB": "AO",
            u"\u09cC": "OW",
            u"\u09cD": "",
            u"\u09cE": "T",
            u"\u09cf": "",

            u"\u09dC": "DD",
            u"\u09dD": "DDH",
            u"\u09dF": "Y",

            u"\u09e0": "R IH",
            u"\u09e1": "L R IH",  # NOT IN USE

            u"\u09f1": "W",  # NOT IN USE

            u"\u02019": "",
            u"\u0200C": "",
            u"\u0200D": "",
            u"\u02013": "",
        },
        {
            # Assamese
            u"\u0981": "N",
            u"\u0982": "N",
            u"\u0983": "HH",
            u"\u0984": "",
            u"\u0985": "AH",
            u"\u0986": "AA",
            u"\u0987": "IH",
            u"\u0988": "IY",
            u"\u0989": "UH",
            u"\u098A": "UW",
            u"\u098B": "R IH",
            u"\u098C": "L R IH",
            u"\u098D": "",
            u"\u098E": "",
            u"\u098F": "EY",

            u"\u0990": "OY",
            u"\u0991": "",
            u"\u0992": "",
            u"\u0993": "AO",
            u"\u0994": "OW",
            u"\u0995": "K",
            u"\u0996": "KH",
            u"\u0997": "G",
            u"\u0998": "GH",
            u"\u0999": "N",
            u"\u099A": "S",
            u"\u099B": "S",
            u"\u099C": "JH",
            u"\u099D": "JHH",
            u"\u099E": "N",
            u"\u099F": "TT",

            u"\u09a0": "TTH",
            u"\u09a1": "DD",
            u"\u09a2": "DDH",
            u"\u09a3": "NN",
            u"\u09a4": "T",
            u"\u09a5": "TH",
            u"\u09a6": "D",
            u"\u09a7": "DH",
            u"\u09a8": "N",
            u"\u09aA": "P",
            u"\u09aB": "F",
            u"\u09aC": "B",
            u"\u09aD": "BH",
            u"\u09aE": "M",
            u"\u09aF": "ZH",

            u"\u09b1": "",
            u"\u09b2": "L",
            u"\u09b3": "",
            u"\u09b4": "",
            u"\u09b5": "",
            u"\u09b6": "HH",
            u"\u09b7": "HH",
            u"\u09b8": "HH",
            u"\u09b9": "HH",
            u"\u09bA": "",
            u"\u09BB": "",
            u"\u09BC": "",
            u"\u09bD": "AH",
            u"\u09bE": "AA",
            u"\u09bF": "IH",

            u"\u09c0": "IY",
            u"\u09c1": "UH",
            u"\u09c2": "UW",
            u"\u09c3": "R IH",
            u"\u09c4": "",
            u"\u09c5": "",
            u"\u09c6": "",
            u"\u09c7": "EY",
            u"\u09c8": "OY",
            u"\u09ca": "",
            u"\u09cB": "AO",
            u"\u09cC": "OW",
            u"\u09cD": "",
            u"\u09cE": "T",
            u"\u09cf": "",

            u"\u09dC": "DD",
            u"\u09dD": "DDH",
            u"\u09dF": "Y",

            u"\u09e0": "R IH",
            u"\u09e1": "L R IH",

            u"\u09b0": "R",
            u"\u09f0": "R",
            u"\u09f1": "W",

            u"\u02019": "",
            u"\u0200C": "",
            u"\u0200D": "",
            u"\u02013": "",
        },
        {

        }
    ]

    def isVowel(self, c):
        # Assamese Bengali
        if u"\u0985" <= c <= u"\u0994":
            return True
        # Odia
        if u"\u0b05" <= c <= u"\u0b14":
            return True
        if u"\u0b60" <= c <= u"\u0b61":
            return True
        # Hindi Marathi
        if u"\u0905" <= c <= u"\u0914":
            return True
        if u"\u0960" <= c <= u"\u0961":
            return True
        if c == u"\u0972":
            return True
        # Gujarati
        if u"\u0a85" <= c <= u"\u0a94":
            return True
        if u"\u0ae0" <= c <= u"\u0ae1":
            return True
        # Punjabi
        if u"\u0a05" <= c <= u"\u0a14":
            return True
        # Malayalam
        if u"\u0d05" <= c <= u"\u0d14":
            return True
        if u"\u0d60" <= c <= u"\u0d61":
            return True
        # Tamil
        if u"\u0b85" <= c <= u"\u0b94":
            return True
        if u"\u0be0" <= c <= u"\u0be1":
            return True
        # Telugu
        if u"\u0c05" <= c <= u"\u0c14":
            return True
        if u"\u0c60" <= c <= u"\u0c61":
            return True
        # Kannada
        if u"\u0c85" <= c <= u"\u0c94":
            return True
        if u"\u0ce0" <= c <= u"\u0ce1":
            return True
        return False

    def isMatra(self, c):
        # Assamese Bengali
        if u"\u09be" <= c <= u"\u09bf":
            return True
        if u"\u09c0" <= c <= u"\u09c4":
            return True
        if u"\u09c7" <= c <= u"\u09c8":
            return True
        if u"\u09cb" <= c <= u"\u09cd":
            return True
        if u"\u09e2" <= c <= u"\u09e3":
            return True

        # Odia
        if u"\u0b3e" <= c <= u"\u0b4d":
            return True
        if u"\u0b62" <= c <= u"\u0b63":
            return True

        # Hindi
        if u"\u093e" <= c <= u"\u094d":
            return True
        if u"\u0962" <= c <= u"\u0963":
            return True

        # Gujarati
        if u"\u0abe" <= c <= u"\u0ac5":
            return True
        if u"\u0ac7" <= c <= u"\u0ac9":
            return True
        if u"\u0acb" <= c <= u"\u0acd":
            return True
        if u"\u0acb" <= c <= u"\u0ace":
            return True
        if u"\u0ae1" <= c <= u"\u0ae2":
            return True

        # Punjabi
        if u"\u0a3e" <= c <= u"\u0a4d":
            return True
        if u"\u0a70" <= c <= u"\u0a71":
            return True
        if c == u"\u0a75":
            return True

        # Malayalam
        if u"\u0d3e" <= c <= u"\u0d44":
            return True
        if u"\u0d46" <= c <= u"\u0d48":
            return True
        if u"\u0d4a" <= c <= u"\u0d4e":
            return True
        if c == u"\u0d57":
            return True
        if u"\u0d62" <= c <= u"\u0d63":
            return True

        # Tamil
        if u"\u0bbe" <= c <= u"\u0bcd":
            return True
        if c == u"\u0bd7":
            return True

        # Telugu
        if u"\u0c3e" <= c <= u"\u0c4d":
            return True
        if u"\u0c55" <= c <= u"\u0c56":
            return True
        if u"\u0c62" <= c <= u"\u0c63":
            return True

        # Kannada
        if u"\u0cbe" <= c <= u"\u0cbf":
            return True
        if u"\u0cc0" <= c <= u"\u0cc4":
            return True
        if u"\u0cc6" <= c <= u"\u0cc8":
            return True
        if u"\u0cca" <= c <= u"\u0ccd":
            return True
        if u"\u0cd5" <= c <= u"\u0cd6":
            return True
        if u"\u0ce2" <= c <= u"\u0ce3":
            return True

        return False

    def isConsonant(self, c):
        # Assamese Bengali
        if (u"\u0995" <= c <= u"\u09bb") or c == u"\u09ce" or (u"\u09d8" <= c <= u"\u09df") or (
                u"\u09f0" <= c <= u"\u09f1"):
            return True
        # Odia
        if (u"\u0b15" <= c <= u"\u0b3b") or (u"\u0b58" <= c <= u"\u0b5f") or c == u"\u0b71":
            return True
        # Hindi Marathi
        if (u"\u0915" <= c <= u"\u093b") or (u"\u0958" <= c <= u"\u095f"):
            return True
        # Gujarati
        if (u"\u0a95" <= c <= u"\u0abb") or (u"\u0ad8" <= c <= u"\u0adf"):
            return True
        # Punjabi
        if (u"\u0a15" <= c <= u"\u0a3b") or (u"\u0a58" <= c <= u"\u0a5f"):
            return True
        # Malayalam
        if u"\u0d15" <= c <= u"\u0d3b":
            return True
        # Tamil
        if u"\u0b95" <= c <= u"\u0bbb":
            return True
        # Telugu
        if (u"\u0c15" <= c <= u"\u0c3b") or (u"\u0c58" <= c <= u"\u0c5f"):
            return True
        # Kannada
        if (u"\u0c95" <= c <= u"\u0cbb") or (u"\u0cd8" <= c <= u"\u0cdf"):
            return True
        return False

    def isModifier(self, c):
        # Assamese Bengali
        if u"\u0981" <= c <= u"\u0983":
            return True
        # Odia
        if u"\u0b01" <= c <= u"\u0b03":
            return True
        # Hindi
        if u"\u0901" <= c <= u"\u0903":
            return True
        # Gujarati
        if u"\u0a81" <= c <= u"\u0a83":
            return True
        # Punjabi
        if u"\u0a01" <= c <= u"\u0a03":
            return True
        # Malayalam
        if u"\u0d01" <= c <= u"\u0d03":
            return True
        # Tamil
        if u"\u0b81" <= c <= u"\u0b83":
            return True
        # Telugu
        if u"\u0c01" <= c <= u"\u0c13":
            return True
        # Kannada
        if u"\u0c81" <= c <= u"\u0c83":
            return True
        return False

    def pronounce(self, input, index):
        # input = pp.normalize(input,index)
        # input = norm.getIndicNormalized(input)
        self.stack = Stacked()
        i=0
        while i<len(input):
            if self.isConsonant(input[i]):
                if input[i] == u"\u09af":
                    if i > 1 and input[i - 1] == u"\u09cd":
                        if input[i - 2] != u"\u09f0" and input[i - 2] != u"\u09b0":
                            self.stack.push(self.phone_map[index][u"\u09df"])
                        else:
                            self.stack.push(self.phone_map[index][input[i]])
                    else:
                        self.stack.push(self.phone_map[index][input[i]])
                elif input[i] == u"\u09b6":
                    if i < len(input) - 2 and input[i + 1] == u"\u09cd":
                        if input[i + 2] == u"\u09f0" or input[i + 2] == u"\u09b0":
                            self.stack.push("SH")
                        elif input[i + 2] == u"\u09ac":
                            self.stack.push(self.phone_map[index][u"\u099a"])
                            i = i + 2
                        else:
                            self.stack.push(self.phone_map[index][u"\u099a"])
                    else:
                        self.stack.push(self.phone_map[index][input[i]])
                elif input[i] == u"\u09b7":
                    if i < len(input) - 1 and input[i + 1] == u"\u09cd":
                        self.stack.push(self.phone_map[index][u"\u099a"])
                    else:
                        self.stack.push(self.phone_map[index][input[i]])
                elif input[i] == u"\u09b8":
                    if i < len(input) - 1 and input[i + 1] == u"\u09cd":
                        self.stack.push(self.phone_map[index][u"\u099a"])
                    else:
                        self.stack.push(self.phone_map[index][input[i]])
                elif input[i] == u"\u0995":
                    if i < len(input) - 2 and input[i + 1] == u"\u09cd" and input[i + 2] == u"\u09b7":
                        self.stack.push("KH")
                        self.stack.push("Y")
                        i = i + 2
                    else:
                        self.stack.push(self.phone_map[index][input[i]])
                elif input[i] == u"\u099c" or input[i] == u"\u091c":
                    if i < len(input) - 2 and input[i + 1] == u"\u09cd":
                        if input[i + 2] == u"\u099e":
                            self.stack.push("G")
                            self.stack.push("Y")
                            i = i + 2
                        elif input[i + 2] == u"\u091e":
                            self.stack.push("G")
                            self.stack.push("Y")
                            i = i + 2
                        else:
                            self.stack.push(self.phone_map[index][input[i]])
                    else:
                        self.stack.push(self.phone_map[index][input[i]])
                else:
                    #print(input[i])
                    self.stack.push(self.phone_map[index][input[i]])
                if i != len(input) - 1:
                    self.stack.push("AH")
                else:
                    # For Odia if the word ends with a consonant without any matras, then add "AH" to phonems.
                    if (u"\u0b15" <= input[i] <= u"\u0b18") or (u"\u0b1a" <= input[i] <= u"\u0b1d") or (
                            u"\u0b1f" <= input[i] <= u"\u0b39") or (u"\u0b5c" <= input[i] <= u"\u0b5d"):
                        self.stack.push("AH")
                self.prevState = self.stateConsonant
            elif self.isVowel(input[i]):
                self.stack.push(self.phone_map[index][input[i]])
                self.prevState = self.stateVowel
            elif self.isMatra(input[i]):
                # if self.prevState != self.stateConsonant:
                #     return "Invalid"
                if self.prevState == self.stateConsonant:
                    self.stack.pop()
                self.stack.push(self.phone_map[index][input[i]])
                self.prevState = self.stateMatra
            # For special signs, anuswar-bisarg-chandrabindu
            elif self.isModifier(input[i]):
                # if self.prevState == -1:
                #     return "Invalid"

                # Change phone mapping of chandrabindu to "M" if succeeding consonant is प फ ब भ म
                # Check if "Chandrabindu" associated character is NOT the last character of a word
                if i < len(input) - 1:
                    if u"\u0901" == input[i] and (u"\u092a" <= input[i+1] <= u"\u092e"):
                        self.stack.push("M")
                    elif u"\u0b01" == input[i] and (u"\u0b2a" <= input[i+1] <= u"\u0b2e"):
                        self.stack.push("M")
                    elif u"\u0981" == input[i] and (u"\u09aa" <= input[i+1] <= u"\u09ae"):
                        self.stack.push("M")
                    else:
                        self.stack.push(self.phone_map[index][input[i]])
                else:
                    self.stack.push(self.phone_map[index][input[i]])
                self.prevState = -1
            i=i+1

        return self.stack.get()


# This is for testing, to be removed/commented
# test = ବଣରେ ଆଉ ଆଗଭଳି ବାଘ ଡର ରହିଲା ନାହିଁ
# input = u"ବଣରେ ଆଉ ଆଗଭଳି ବାଘ ଡର ରହିଲା ନାହିଁ"
# input = u"पँ"

# input = u"সূর্য"
# input = u"অ্যাকাউন্ট"
# list = []
# inputTokens = input.split(" ")
mappings = Mappings()
print(mappings.pronounce(u"अमन", cs.Hindi))

# for token in inputTokens:
#     list.append(token.strip() + "\t" + mappings.pronounce(token, cs.Hindi) + "\n")
#     list.append(token.encode('utf-8').strip() + "\t" + mappings.pronounce(token, cs.Hindi) + "\n")



