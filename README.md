# Int1C 

Simple implementation of ones' complement integers.

## AGC details

### Instructions

Definitions to be added.

Instructions are composed of one or more subinstruction commands (e.g. MP0, MP1, MP3 for MP). Each 

### Registers

Name | Bits | Description
---- | ---- | -----------
A    | 16   | Accumulator
B    | 16   | Terminal register
C    | 16   | Complement of B
CP   | X    | The register pointed to by the address in S 
G    | 16   | Memory buffer register
L    | 16   | Lower order accumulator
S    | 12   | Address register
SQ   | 7    | Sequence register, containing EXT, 3 SQ bits plus 3 extra bits
U    | 16   | Adder output gates
WL   | 16   | Write lines (bus)
X    | 16   | Adder input 1
Y    | 16   | Adder input 2
Z    | 16   | Program counter

### Flip-flops

Name              | Description
----------------- | -----------
CI flip-flop      | End around carry
Stage 1 flip-flop | Stage counter
Stage 2 flip-flop | Stage counter
BR1 flip-flop     | Branch register
BR2 flip-flop     | Branch register
Ext flip-flop     | Extend bit

### Control pulses

Taken from Table 4-V1, page 4-73 of the LEM System Manual Volume 1, 1966 version.

Control pulse MCRO is mentioned by not defined.

Name   | Description
------ | -----------
A2X    | Enter bits 16 trough 1 of register A directly (not via WL's) into bit positions 16 through 1 of register X.
B15X   | Enter a logic ONE into bit position 15 of register X.
CI     | Insert carry bit into position 1 of the adder.
CLXC   | Clear register X if flip-flop BR1 contains a logic ZERO. (Used in divide instruction.)
DVST   | Advance the Gray code content of the stage counter by complementing the content of the next higher bit position as shown below.
EXT    | Enter a logic ONE into bit position EXT of register SQ.
G2LS   | Enter bits 16 through 4 and 1 of register G into bit positions 16, 15, and 12 through 1 of register X. See control pulse ZAP.
KRPT   | Rest interrupt priority cells.
L16    | Enter a logic ONE into bit position 16 of register L.
L2GD   | Enter bits 16 and 14 through 1 of register L into bit positions 16 through 2 of register G; enter a logic ONE (pulse MCRO) into bit position 1 of register G.
MONEX  | Clear register X, then enter logic ONE's into bit positions 16 through 2.
MOUT   | Generate one negative rate output pulse.
NEACOF | Permit end around carry upon completion of subinstruction MP3.
NEACON | Inhibit end around carry (also during WYD) until NEACOF.
NISQ   | Load next instruction into register SQ. Also frees certain restrictions; permits execution of instruction RUPT and counter instructions. See control pulses RB and WSQ.
PIFL   | Prevent interflow on control puse WYD if bit position 15 of register L contains a logic ONE; block writing into bit position 1 of register Y. See control pulse WYD.
PONEX  | Clear register X, then enter a logic ONE into bit position 1.
POUT   | Generate one positive rate output pulse.
PTWOX  | Clear register X, then enter a ONE into bit position 2.
R15    | Place octal 15 on WL's
R1C    | Place octal 177776 (minus one) on WL's.
RA     | Read bits 16 through 1 of register A to WL's 16 through 1.
RAD    | Read address of next cycle. RAD appears at the end of an instruction and is normally interpreted as RG. If the next instruction is INHINT, RELINT or EXTEND, RAD is interpreted as RZ and ST2 instead.
RB     | Read bits 16 through 1 of register B to WL's 16 through 1.
RB1    | Place octal 1 on WL's.
RB1F   | Place octal 1 on WL's if flip-flop BR1 contains a logic ONE.
RB2    | Place octal 2 on WL's.
RC     | Read the complemented contents of register B (bits 16 through 1 of C) to WL's 16 through 1.
RCH    | Read the contents of the input of output channel specified by the contents of register S; bit 16 is read to WL's 16 and 15 and bits 14 through 1 are read to WL's 14 through 1.
REB    | Read bits 11, 10, and 9 of register EB to WL's 11, 10, and 9. See control pulse RSC.
RFB    | Read bits 16 and 14 through 11 of register FB to WL's 16 and 14 through 11. See control pulse RSC.
RG     | Read bits 16 through 1 of register G to WL's 16 through 1.
RL     | Read bit 16 of register L to WL's 16 and 15, and bits 14 through 1 to WL's 14 through 1.
RL10BB | Read low 10 bits of register B to WL's 10 through 1.
RQ     | Read bits 16 through 1 of register Q to WL's 16 through 1.
RRPA   | Place on WL's the address of the priority program requested.
RSC    | Read the content of register CP defined by the content of register S; bits 16 through 1 are read to WL's 16 through 1.
RSCT   | Place on WL's the address of the counter to be incremented.
RSTRT  | Place octal 4000 (start address) on WL's.
RSTSTG | Reset the stage counter.
RU     | Read bits 16 through 1 of adder output gates (U) to WL's 16 through 1.
RUS    | Read bit 15 of adder output gates (U) to WL's 16 and 15, and bits 14 through 1 to WL's 14 through 1.
RZ     | Read bits 16 through 1 of register Z to WL's 16 through 1.
ST1    | Set stage 1 flip-flop to logic ONE at next time 12. [bit 1 of stage counter]
ST2    | Set stage 2 flip-flop to logic ONE at next time 12. [bit 2 of stage counter]
STAGE  | Execute next subinstruction as defined by the content of the divide stage counter.
STD2   | ?
TL15   | Copy bit 15 of register L into flip-flop BR1.
TMZ    | Test for minus zero; if bits 16 through 1 are all logic ONE's, set flip-flop BR2 to logic ONE; ohterwise set BR2 to logic ZERO.
TOV    | Test for overflow: set flip-flops BR1 and BR2 to 01 if positive overflow , to 10 if negative overflow.
TPZG   | Test content of register G for plus zero: if bits 16 through 1 are all logic ZERO's, set flip-flop BR2 to logic ONE; otherwise do not change content of BR2.
TRSM   | Test for the resume address (0017) during instruction NDX.
TSGN   | Test sign (bit 16): if a logic ZERO, set flip-flop BR1 to to logic ZERO; if a logic ONE, set flip-flop BR1 to logic ONE.
TSGN2  | Test sign (bit 16): if a logic ZERO, set flip-flop BR2 to to logic ZERO; if a logic ONE, set flip-flop BR2 to logic ONE.
TSGU   | Test sign (bit 16) of sum contained in adder output gates (U): if a logic ZERO, set flip-flop BR1 to logic ZERO; if a logic ONE, set flip-flop BR1 to logic ONE.
U2BBK  | Enter bits 16 and 14 through 11 of output gates U directly into register FB and bits 3, 2, and 1 of gates U intou bits 11, 10, and 9 of register EB.
WA     | Clear register A and write the contents of WL's 16 through 1 into bit positions 16 through 1.
WALS   | Clear register A and write the contents of WL's 16 through 3 into bit positions 14 through 1; if bit position 1 of register G contains a logic ZERO, the content of bit position 16 of register G is entered into bit position 16 and 15 of register A; if bit position 1 of register G contains a logic ONE, the contents of output gate U 16 of the adder is entered into bit positions 16 and 15 of register A; clear bits 14 and 13 of register L and write the contents of WL's 2 and 1 into bit positions 14 and 13. See control pulse ZAP.
WB     | Clear register B and write the contents of WL's 16 through 1 into bit positions 16 through 1.
WBBK   | Clear registers EB and FB and write the content of WL's 16 and 14 through 11 into register FB and content of WL's 3, 2, and 1 into register EB. See control pulse WSC.
WCH    | Clear the channel specified by the contents of register S (bits 9 through 1) and write the contents of WL's 16 through 1 into this channel. 
WEB    | Clear register EB and write the contents of WL's 11, 10, and 9 into bit positions 11, 10, and 9. See control pulse WSC.
WFB    | Clear register FB and write the contents of WL's 16 and 14 through 11 into bit positions 16 and 14 through 11. See control pulse WSC.
WG     | Clear register G and write the contents of WL's 16 through 1 into bit positions 16 through 1 (except if register S contains octal addresses 20 through 23).
WL     | Clear register L and write the contents of WL's 16 through 1 into bit positions 16 through 1.
WOVR   | Test for positive overflow. If register S ontains 0025, counter 0024 is incremented; if register S contains 0026, 0027, or 0030, instruction RUPT is executed.
WQ     | Clear register Q and write the contents of WL's 16 through 1 into bit positions 16 through 1. 
WS     | Clear register S and write the contents of WL's 12 through 1 into bit positions 12 through 1.
WSC    | Clear the CP register specified by the contents of register S and write the contents of WL's 16 through 1 into bit positions 16 through 1 of this register.
WSQ    | Clear register SQ and write the contents of WL's 16 and 14 through 10 into bit positions 16 and 14 through 10, copy the content of the extend flip-flop into bit positions EXT of register Q. See control pulse NISQ. 
WY     | Clear registers X and Y; write the contents of WL's 16 through 1 into bit positions 16 through 1 of register Y.
WY12   | Clear registers X and Y; write the contents of WL's 12 through 1 into bit positions 12 through 1 of register Y.
WYD    | Clear registers X and Y; write the contents of WL's 16 and 14 through 1 into bit positions 16 and 15 through 2 of register Y; write the content of WL 16 into bit position 1 of register Y except in SHINC sequence, or unless bit 15 of register L is a logic ONE at PIFL, or if end around carry is inhibited (NEACON).
WZ     | Clear register Z and write the contents of WL's 16 through 1 into bit positions 16 through 1.
Z15    | Enter a logic ONE into bit position 15 of register Z.
Z16    | Enter a logic ONE into bit position 16 of register Z.
ZAP    | Generate control pulses RU, G2LS, and WALS.
ZIP    | Generate control pulses A2X and L2GD; also perform read/write operations depending on the content of bit positions 15, 2, and 1 of register L as shown below.
ZOUT   | Generate no rate output pulse.

#### DVST complementing operations

Binary | Octal
------ | -----
000    | 0
001    | 1
011    | 3
111    | 7
110    | 6
100    | 4

#### ZIP Read/Write operations

L15 | L2 | L1 | Read | Write | Carry | Remember 
--- | -- | -- | ---- | ----- | ----- | --------
 0  | 0  | 0  | -    | WY    | -     | -
 0  | 0  | 1  | RB   | WY    | -     | -
 0  | 1  | 0  | RB   | WYD   | -     | -
 0  | 1  | 1  | RC   | WY    | CI    | MCRO
 1  | 0  | 0  | RB   | WY    | -     | -
 1  | 0  | 1  | RB   | WYD   | -     | -
 1  | 1  | 0  | RC   | WY    | CI    | MCRO
 1  | 1  | 1  | -    | WY    | -     | MCRO


## TS: Transfer to storage

### TS0

 1) RL10BB WS
 2) RSC WG
 3) RA WB TDV
 4) RZ WY12
    00: - (A16,15 = 00 or A16,15 = 11)
    01: CI (A16,15 = 01) overflow
    10: CI (A16,15 = 10) underflow
 5) 00: -
    01: RB1 WA
    10: RC,R1C WA
 6) RU WZ
 7) RB WSC WG
 8) RZ WS ST2
  

## Addition

### AD0

 1) 
 2) RSC WG
 3)
 4)
 5)
 6)
 7) RG WB
 8) RZ WS ST2
 9) RB WG
10) RB WY A2X
11) RU WA

So:
memory location to G
G to B

Z to S (plus stage counter) WHY?
B to G WHY?
B to Y, A to X direct
U to A
 
## Multiplication


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