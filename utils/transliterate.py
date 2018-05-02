# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 08:10:03 2017

@author: pankaj-t430
"""
AA	odd     AA D
        AE	at	AE T
        AH	hut	HH AH T
        AO	ought	AO T
        AW	cow	K AW
        AY	hide	HH AY D
        B 	be	B IY
        CH	cheese	CH IY Z
        D 	dee	D IY
        DH	thee	DH IY
        EH	Ed	EH D
        ER	hurt	HH ER T
        EY	ate	EY T
        F 	fee	F IY
        G 	green	G R IY N
        HH	he	HH IY
        IH	it	IH T
        IY	eat	IY T
        JH	gee	JH IY
        K 	key	K IY
        L 	lee	L IY
        M 	me	M IY
        N 	knee	N IY
        NG	ping	P IH NG
        OW	oat	OW T
        OY	toy	T OY
        P 	pee	P IY
        R 	read	R IY D
        S 	sea	S IY
        SH	she	SH IY
        T 	tea	T IY
        TH	theta	TH EY T AH
        UH	hood	HH UH D
        UW	two	T UW
        V 	vee	V IY
        W 	we	W IY
        Y 	yield	Y IY L D
        Z 	zee	Z IY
        ZH	seizure	S IY ZH ER
vw_phn_map = {
				"AA":{"आ":"ा"},
				"AE":{"ऐ":"ै"},
				"AH":{"अ"":""},
				"AO":{"औ":"ौ"},
				"AW":{"आउ":"ाउ"},
				"AY":{"आई":"ाई"},
				"EH":{"ऍ":"ॅ"},
				"EY":{"ए":"े"},
				"IH":{"इ":"ि"},
				"IY":{"ई":"ी"},
				"OW":{"ओ":"ो"},
				"OY":{"ऑय":"ॉय"},
				"UH":{"उ":"ु"},
				"UW":{"ऊ":"ू"},
			 }

char_map = {
			 "K":"क",
			 "B":"ब",
			 "CH":"च",
			 "D":"ड",
			 "
		   }
			 
inword = ["S","IH","NG","ER"]		