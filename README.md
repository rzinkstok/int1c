# Int1C 

Simple implementation of ones' complement integers.

## Multiplication

### AGC control pulses


#### ZIP

A2X L2GD and:

L15 | L2 | L1 | READ | WRITE | CARRY | REMEMBER 
--- | -- | -- | ---- | ----- | ----- | --------
 0  |  0 |  0 |   -  |  WY   | -     | -
 
 
 0   0  1    RB   WY    -     -
 0   1  0    RB   WYD   -     -
 0   1  1    RC   WY    CI    MCRO
 1   0  0    RB   WY    -     -
 1   0  1    RB   WYD   -     -
 1   1  0    RC   WY    CI    MCRO
 1   1  1    -    WY    -     MCRO


#### ZAP

RU G2LS WALS

### AGC multiplication, 1966 version

#### MP0

 1) 
 2) RSC WG
 3) RA WB TSGN
 4) 0X: RB WL (A16 = 0)
    1X: RC WL (A16 = 1)
 5) 
 6) 
 7) RG WB TSGN2
 8) RZ WS
 9) 00: RB WY (A16 = 0, G16 = 0)
    01: RB WY CI L16 (A16 = 0, G16 = 1)
    10: RC WY CI L16 (A16 = 1, G16 = 0)
    11: RC WY (A16 = 1, G16 = 1)
10) RU WB TSGN ST1 NEACON
11) 0X: WA (U16 = 0)
    1X: RB1 R1C (U16 = 1)
12) 

#### MP1

 1) ZIP
 2) ZAP
 3) ZIP
 4) ZAP
 5) ZIP
 6) ZAP
 7) ZIP
 8) ZAP
 9) ZIP
10) ZAP ST1 ST2
11) ZIP

#### MP3

 1) ZAP
 2) ZIP NISQ
 3) ZAP
 4) RSC WG
 5) RZ WY12 CI
 6) RU WZ TL15 NEACOF
 7) 0X: - (U15 = 0)
    1X: RB WY A2X (U15 = 1)
 8) RA0 WB WS
 9) RA
10) RL
11) 0X: - (U15 = 0)
    1X: RU WA (U15 = 1)

### AGC multiplication, Memo 9 version

#### MP0

 1) 
 2) RSC WG
 3) RA WB TSGN
 4) 1X: RB WL
    0X: RC WL
 5) 
 6) 
 7) RG WB TSGN2
 8) RZ WS
 9) 00: RB WY
    01: RB WY CI
    10: RC WY CI
    11: RC WY
10) RU WB TSGN ST1 NEACON
11) 0X: WA
    1X: WA RB1 R1C L16
    
#### MP1
 
 1) ZIP
 2) ZAP
 3) ZIP
 4) ZAP
 5) ZIP
 6) ZAP
 7) ZIP
 8) ZAP
 9) ZIP
10) ZAP ST1 ST2
11) ZIP

#### MP3

 1) ZAP
 2) ZIP NISQ
 3) ZAP
 4) RSC WG
 5) RZ WY12 CI
 6) RU WZ TL15 NEACOF
 7) 0X: -
    1X: RB WY A2X
 8) RAD WB WS
 9) RA
10) RL
11) 0X: -
    1X: RU WA