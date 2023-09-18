# -*- coding:utf-8 -*-
import copy
import io
import math
import struct

KEY_BASE = 0x7C89
KEY_ADVANCE = 0x2983
KEY_VARIABLE = 0x0010
KEY_TERMINATOR = 0x0000
KEY_TEXTRETURN = 0xBE00
KEY_TEXTCLEAR = 0xBE01
KEY_TEXTWAIT = 0xBE02
KEY_TEXTNULL = 0xBDFF
KEY_TEXTRUBY = 0xFF01

lineOffsets = []
f: io.BufferedReader




def binary2str(f: io.BufferedReader):
    sections, = struct.unpack('<H', f.read(2))
    entryCount, = struct.unpack('<H', f.read(2))
    totalLength, = struct.unpack('<I', f.read(4))
    initialKey, = struct.unpack('<I', f.read(4))
    sectionDataOffset, = struct.unpack('<I', f.read(4))
    f.seek(sectionDataOffset)
    v, = struct.unpack('<I', f.read(4))
    for i in range(0, entryCount):
        offset, = struct.unpack('<i', f.read(4))
        length, extra = struct.unpack('<2h', f.read(4))
        offset += sectionDataOffset
        lineOffsets.append({
            'offset': offset,
            'length': length,
            'extra': extra
        })
    arr = generateLineData(f)
    # print(arr)
    testStrOutput(arr)

## 38 22 F9 12 4E A6 10 30 45
def cryptLineData(data: bytes, key: int):
    result = copy.copy(data)
    length = result.__len__()
    res: list[int] = []
    for i in range(0, length, 2):
        res.append(result[i] ^ (key % 0x100))
        res.append(result[i + 1] ^ ((key >> 8) % 0x100))
        key = (key << 3 | key >> 13) % 0x10000
    return res


def getLineKey(index: int):
    key = KEY_BASE
    for i in range(0, index):
        key += KEY_ADVANCE
    return key


def generateLineData(f: io.BufferedReader):
    arr: list[list[int]] = []
    maxLength = lineOffsets.__len__()
    key = KEY_BASE
    for i in range(0, maxLength):
        lineOffset = lineOffsets[i]
        f.seek(lineOffset['offset'])
        encryptedData = f.read(2 * lineOffset['length'])
        info = cryptLineData(encryptedData, key)
        key += KEY_ADVANCE
        key = key & 0xffff
        arr.append(info)
    return arr


def GetLineString(data: list[int]):
    s = ''
    i = 0
    bData = bytes(data)
    while i < data.__len__():
        val = struct.unpack_from("<H", bData, i)[0]
        if val == KEY_TERMINATOR:
            return s
        elif (val == KEY_VARIABLE):
            s += "[VAR]"
        elif (val == "\n"):
            s += "\n"
        elif (val == "\\"):
            s += "\\"
        elif (val == "["):
            s += "\["
        else:
            s += chr(val)
        i += 2
    return s


def getVariableString():
    pass


def testStrOutput(data: list[list[int]]):
    for arr in data:
        str = GetLineString(arr)
        print(str)