
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

directionVec3 = mc.player.getDirection() # プレイヤーの方向の取得

d_x, d_y, d_z = directionVec3 # ベクトルを出力

#print(d_x, d_y, d_z)

# 方向の決定(北:1, 南:2, 西:3, 東:4)
if d_z**2 > d_x**2:
   if d_z > 0:
       direction = 1
   else:
       direction = 2
elif d_x**2 > d_z**2:
   if d_x > 0:
       direction = 3
   else:
       direction = 4
       
print(direction)
   
# 道路構造リストの作成(道路幅3m、高さ3m、路側帯2m)

l = input("道路の延長は？: ")
l = int(l)

BlockList = [[0 for n in range(7)] for m in range(4)]  #とりあえず枠つくっといて

BlockList[0]=[2,2,1,1,1,2,2]

#for n in range(3):
#   n = n + 2
#   BlockList[0][n] = 1
   
#for m in range(2):
#   BlockList[0][m] = 2

#for o in range(2):
#   o = o + 5
#   BlockList[0][o] = 2
   
#print(BlockList[0][5])


#　道路の作成
x, y, z = mc.player.getPos() # 現在位置の取得

#if direction == 1:
#   x = x + 3
#   y = y - 1
                       
   #for dz in range(l):
   #    for dy in range(4):
   #        for dx in range(7):
   #            for i in range(4):
   #                for j in range(7):
   #                    mc.setBlock(x - dx, y + dy, z + dz, BlockList[i][j])

#for i in range(l):
#    for j in range(7):
#        for k in range(4):
#            mc.setBlock(x + j, y + k, z + i, BlockList[k][j])

for i in range(7):
    for j range(4):
        mc.setBlocks(x + i,y + j,z,x + i,y + j,z + l,BlockList[j][i])

mc.postToChat("Finish!")