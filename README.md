# Int1C 

Simple implementation of ones' complement integers.

## Multiplication

### AGC registers

Name | Bits | Description
---- | ---- | -----------
A  | 16 | Accumulator
B  | 16 | Terminal register
C  | 16 | Complement of B
CP | ?  | The register pointed to by the address in S 
G  | 6  | Memory buffer register
L  | 16 | Lower order accumulator
S  | 12 | Address register
SQ | 7  | Sequence register
U  | 16 | Adder output gates
WL | 16 | Write lines (bus)
X  | 16 | Adder input 1
Y  | 16 | Adder input 2
Z  | 16 | Program counter

### Other parts
Name              | Description
----------------- | -----------
CI flip-flop      | End around carry
Stage 1 flip-flop | Stage counter
Stage 2 flip-flop | Stage counter
BR1 flip-flop     | Branch register
BR2 flip-flop     | Branch register

### AGC control pulses

Name   | Description
------ | -----------
A2X    | Enter bits 16 trough 1 of register A directly (not via WL's) into bit positions 16 through 1 of register X.
CI     | Insert carry bit into position 1 of the adder.
G2LS   | Enter bits 16 through 4 and 1 of register G into bit positions 16, 15, and 12 through 1 of register X. See control pulse ZAP.
L16    | Enter a logic ONE into bit position 16 of register L.
L2GD   | Enter bits 16 and 14 through 1 of register L into bit positions 16 through 2 of register G; enter a logic ONE (pulse MCRO) into bit position 1 of register G.
NEACOF | Permit end around carry upon completion of subinstruction MP3.
NEACON | Inhibit end around carry (also during WYD) until NEACOF.
NISQ   | Load next instruction into register SQ. Also frees certain restrictions; permits execution of instruction RUPT and counter instructions. See control pulses RB and WSQ.
R1C    | Place octal 177776 (minus one) on WL's.
RA     | Read bits 16 through 1 of register A to WL's 16 through 1.
RB     | Read bits 16 through 1 of register B to WL's 16 through 1.
RB1    | Place octal 1 on WL's.
RC     | Read the complemented contents of register B (bits 16 through 1 of C) to WL's 16 through 1.
RG     | Read bits 16 through 1 of register G to WL's 16 through 1.
RL     | Read bit 16 of register L to WL's 16 and 15, and bits 14 through 1 to WL's 14 through 1.
RSC    | Read the content of register CP defined by the content of register S; bits 16 through 1 are read to WL's 16 through 1.
RU     | Read bits 16 through 1 of adder output gates (U) to WL's 16 through 1.
RZ     | Read bits 16 through 1 of register Z to WL's 16 through 1.
ST1    | Set stage 1 flip-flop to logic ONE at next time 12.
ST2    | Set stage 2 flip-flop to logic ONE at next time 12.
TL15   | Copy bit 15 of register L into flip-flop BR1.
TSGN   | Test sign (bit 16): if a logic ZERO, set flip-flop BR1 to to logic ZERO; if a logic ONE, set flip-flop BR1 to logic ONE.
TSGN2  | Test sign (bit 16): if a logic ZERO, set flip-flop BR2 to to logic ZERO; if a logic ONE, set flip-flop BR2 to logic ONE.
WA     | Clear register A and write the contents of WL's 16 through 1 into bit positions 16 through 1.
WALS   | Clear register A and write the contents of WL's 16 through 3 into bit positions 14 through 1; if bit position 1 of register G contains a logic ZERO, the content of bit position 16 of register G is entered into bit position 16 and 15 of register A; if bit position 1 of register G contains a logic ONE, the contents of output gate U 16 of the adder is entered into bit positions 16 and 15 of register A; clear bits 14 and 13 of register L and write the contents of WL's 2 and 1 into bit positions 14 and 13. See control pulse ZAP.
WB     | Clear register B and write the contents of WL's 16 through 1 into bit positions 16 through 1.
WG     | Clear register G and write the contents of WL's 16 through 1 into bit positions 16 through 1 (except if register S contains octal addresses 20 through 23).
WL     | Clear register L and write the contents of WL's 16 through 1 into bit positions 16 through 1.
WY     | Clear registers X and Y; write the contents of WL's 16 through 1 into bit positions 16 through 1 of register Y.
WY12   | Clear registers X and Y; write the contents of WL's 12 through 1 into bit positions 12 through 1 of register Y.
WYD    | Clear registers X and Y; write the contents of WL's 16 and 14 through 1 into bit positions 16 and 15 through 2 of register Y; write the content of WL 16 into bit position 1 of register Y except in SHINC sequence, or unless bit 15 of register L is a logic ONE at PIFL, or if end around carry is inhibited (NEACON).
WZ     | Clear register Z and write the contents of WL's 16 through 1 into bit positions 16 through 1.


#### ZIP

A2X L2GD and:

L15 | L2 | L1 | READ | WRITE | CARRY | REMEMBER 
--- | -- | -- | ---- | ----- | ----- | --------
 0  | 0  | 0  | -    | WY    | -     | -
 0  | 0  | 1  | RB   | WY    | -     | -
 0  | 1  | 0  | RB   | WYD   | -     | -
 0  | 1  | 1  | RC   | WY    | CI    | MCRO
 1  | 0  | 0  | RB   | WY    | -     | -
 1  | 0  | 1  | RB   | WYD   | -     | -
 1  | 1  | 0  | RC   | WY    | CI    | MCRO
 1  | 1  | 1  | -    | WY    | -     | MCRO


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