"""
Your goal is to create a function that returns a list with a string for each of the 108 tiles in the following format:

"rank suit"
Where rank is a number from 1 to 9 and suit is one of the three suits (tong, tiao, wan), both written in the pinyin transcription of Mandarin Chinese (for numbers see table below).

Number	Character	Pinyin
1	一	yi
2	二	er
3	三	san
4	四	si
5	五	wu
6	六	liu
7	七	qi
8	八	ba
9	九	jiu
Three of the tiles have special names. Each of the 4 copies of these tiles should be represented by their names only (no suit, no rank):

One of tong is called bing gan (饼干, cookie)
Two of tong is called yan jing (眼镜, glasses)
One of tiao is called ji (鸡, chicken)
Examples of tiles
Five of tong ➞ "wu tong"

Seven of wan ➞ "qi wan"

One of tiao ➞ "ji"

Three of tiao ➞ "san tiao"
Notes
Don't forget to include 4 copies of each tile.
Don't forget to substitute the tiles with special names.
You can return the tiles in any order.
"""

def gen_tiles():
    tiles = []
    ranks = ["yi", "er", "san", "si", "wu", "liu", "qi", "ba", "jiu"]
    suits = ["tong", "tiao", "wan"]
    special_tiles = {"1tong": "bing gan", "2tong": "yan jing", "1tiao": "ji"}

    for rank in ranks:
        for suit in suits:
            for _ in range(4):
                tiles.append(f"{rank} {suit}")
    for tile in special_tiles:
        for _ in range(4):
            tiles.remove(tile)
            tiles.append(special_tiles[tile])
    
    return tiles

tiles = gen_tiles()
print(len(tiles))
print(tiles[:10])