import cv2
import math
import numpy as np
import time

## 我的canny代码
def mycanny(img_g, TL, TH):
    neighbor_num = 1
    ## sobel
    start_mycanny = time.time()  
    # sobelx = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
    # sobely = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
    # img_b = cv2.copyMakeBorder(img, 1, 1, 1, 1, cv2.BORDER_REPLICATE) #产生边界方便之后和sobel算子相乘
    # img_dx = np.zeros(img.shape, dtype="int8")
    # img_dy = np.zeros(img.shape, dtype="int8")
    img_dxy = np.zeros(img_g.shape, dtype="int")
    theta = np.zeros(img_g.shape, dtype="float")
    # for i in range(1, img_b.shape[0]-1):
    #     for j in range(1, img_b.shape[1]-1):
    #         dx = np.sum(img_b[i-1:i+2, j-1:j+2]*sobelx)
    #         dy = np.sum(img_b[i-1:i+2, j-1:j+2]*sobely)
    #         img_dx[i-1][j-1] = dx
    #         img_dy[i-1][j-1] = dy
    # #             img_dxy[i-1][j-1] = np.sqrt(img_dx[i-1][j-1]**2+img_dy[i-1][j-1]**2)
    #         img_dxy[i-1][j-1] = np.sqrt(dx**2+dy**2)
    #         theta[i-1][j-1] = math.atan2(dy, dx)*180/np.pi

    sobelx = cv2.Sobel(img_g,cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(img_g,cv2.CV_64F, 0, 1, ksize=3)
    for i in range(0, img_g.shape[0]):
        for j in range(0, img_g.shape[1]):
            dx = sobelx[i][j]
            dy = sobely[i][j]
    #         img_dx[i-1][j-1] = dx
    #         img_dy[i-1][j-1] = dy
            img_dxy[i-1][j-1] = int(np.sqrt(dx**2+dy**2))
            theta[i-1][j-1] = math.atan2(dy, dx)*180/np.pi
    # img_dxyc = np.zeros(img.shape, dtype="uint8")
    # for i in range(img_dxyc.shape[0]):
    #     for j in range(img_dxyc.shape[1]):
    #         img_dxyc[i][j] = np.sqrt(sobelxk[i][j]**2+sobelyk[i][j]**2)

    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows()

    ## Maximum suppression
    img_yz = np.zeros(img_g.shape, dtype="int") #极大值抑制矩阵初始化
    for i in range(1, img_yz.shape[0]-1):
        for j in range(1, img_yz.shape[1]-1):  #找到梯度方向之后与该方向上的两个像素点比较
            if abs(theta[i][j]) < 22.5 or abs(theta[i][j]) >= 157.5:
                if img_dxy[i][j] >= img_dxy[i][j-1] and img_dxy[i][j] >= img_dxy[i][j+1]:
                    img_yz[i][j] = img_dxy[i][j]
            elif (theta[i][j] >= 22.5 and theta[i][j] < 67.5) or (theta[i][j] >= -157.5 and theta[i][j] < -112.5):
                if img_dxy[i][j] >= img_dxy[i-1][j-1] and img_dxy[i][j] >= img_dxy[i+1][j+1]:
                    img_yz[i][j] = img_dxy[i][j]
            elif (theta[i][j] >= 67.5 and theta[i][j] < 112.5) or (theta[i][j] >= -112.5 and theta[i][j] < -67.5):
                if img_dxy[i][j] >= img_dxy[i-1][j] and img_dxy[i][j] >= img_dxy[i+1][j]:
                    img_yz[i][j] = img_dxy[i][j]
            elif (theta[i][j] >= 112.5 and theta[i][j] < 157.5) or (theta[i][j] >= -67.5 and theta[i][j] < -22.5):
                if img_dxy[i][j] >= img_dxy[i-1][j+1] and img_dxy[i][j] >= img_dxy[i+1][j-1]:
                    img_yz[i][j] = img_dxy[i][j]
    max_yz = np.max(img_yz)
    img_yzs = np.zeros(img_g.shape, dtype="uint8")
    for i in range(1, img_yzs.shape[0]-1):
        for j in range(1, img_yzs.shape[1]-1):
            img_yzs[i][j] = img_yz[i][j]*255//max_yz
    ## Dual threshold detection and edge connection
    img_syz = np.zeros(img_g.shape, dtype="uint8") #双边阈值之后矩阵初始化

    # dfs_h = np.zeros(img_g.shape, dtype="uint8")
    def dfs(img_yz, img_syz, x, y):
        if img_syz[x][y] != 0:
            return 
#         img_syz[x][y] = max(img_yz[x][y]*255//max_yz, 1)
        img_syz[x][y] = 255
        for i in range(-neighbor_num, neighbor_num+1):
            for j in range(-neighbor_num, neighbor_num+1):
                if i == 0 and j == 0:
                    continue
                if x+i >=0 and x+i<img_syz.shape[0] and y+j>=0 and y+j<img_syz.shape[1] and img_yz[x+i][y+j]>=TL:
                    dfs(img_yz, img_syz, x+i, y+j)

    for i in range(0, img_syz.shape[0]):
        for j in range(0, img_syz.shape[1]):
            if img_yz[i][j] >= TH:
                dfs(img_yz, img_syz, i, j)
    #         elif img_yz[i][j] >= TL and img_yz[i][j] < TH:
    #             if img_yz[i-1][j-1] >= TH or img_yz[i][j-1] >= TH or img_yz[i+1][j-1] >= TH or img_yz[i-1][j] >= TH or \
    #                img_yz[i+1][j] >= TH or img_yz[i-1][j+1] >= TH or img_yz[i][j+1] >= TH or img_yz[i+1][j+1]>= TH:
    #                 img_yz[i][j] = TH
    #                 img_syz[i][j] = 255
    end_mycanny = time.time() 
    print("my_canny所需时间%f"%(end_mycanny-start_mycanny))
    ## visualization
    #     cv2.imshow('dx', img_dx)
    #     cv2.imshow('dy', img_dy)
    # cv2.imshow('dxy', img_dxy)
    # cv2.imshow('dxyc', img_dxyc)
    #     cv2.imshow('yz', img_yz)
    # cv2.imshow('syz', img_syz)
    #     cv2.imwrite('yz_me.jpg', img_yz)
    # cv2.imwrite('my_canny33.jpg', img_syz)
    # cv2.imwrite('my_canny33_wsyz.jpg', img_yzs)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    ##              
    # my_houghcircle(img_g, 50, 100)
    return img_syz

##我的houghcircle代码
def myhoughcircle(img_g, canny, r_min, r_max, min_dist, max_dist):
    img_c = np.zeros(img_g.shape, dtype="int")  #用于计数的矩阵
    img_cc = np.zeros(img_g.shape, dtype="uint8")

    r_min1 = 50
    r_max1 = 500
    hwid = 2


    sobelxk = cv2.Sobel(img_g,cv2.CV_16S, 1, 0, ksize=3)
    sobelyk = cv2.Sobel(img_g,cv2.CV_16S, 0, 1, ksize=3)
    dic = {}
    for i in range(0, img_g.shape[0]):
        for j in range(0, img_g.shape[1]):
            if canny[i][j] !=0 and (sobelxk[i][j]!=0 or sobelyk[i][j]!=0):  ##是边缘像素点
                flag = 1
                dx = sobelxk[i][j]
                dy = sobelyk[i][j]
                mag = np.sqrt(dx**2+dy**2)
                for r in range(r_min1, r_max1, 1): ##找到圆周线的法线上的点，并且每次以最小半径为单位增加
                    x_tmp = i+int(round(r*dy/mag)) 
                    y_tmp = j+int(round(r*dx/mag))
    #                 if x_tmp > img_g.shape[0]-1 or x_tmp < 0 or y_tmp < 0 or y_tmp> img_g.shape[1]-1: ##边界条件判断
    #                     break
    #                 img_c[x_tmp][y_tmp] += 1
                    if x_tmp >= img.shape[0]-hwid or x_tmp < hwid or y_tmp < hwid or y_tmp>= img.shape[1]-hwid: ##边界条件判断
                        break
                    for i2 in range(-hwid,hwid+1): ##半径宽度使得法线上点四周更多点计数加一
                        for j2 in range(-hwid,hwid+1):
                            img_c[x_tmp+i2][y_tmp+j2] += 1 
                for r in range(r_min1, r_max1, 1):##找到圆周线的法线上的点，并且每次以最小半径为单位减少
                    x_tmp = i-int(round(r*dy/mag))
                    y_tmp = j-int(round(r*dx/mag))
    #                 if x_tmp > img_g.shape[0]-1 or x_tmp < 0 or y_tmp < 0 or y_tmp> img_g.shape[1]-1: ##边界条件判断
    #                     break
    #                 img_c[x_tmp][y_tmp] += 3
                    if x_tmp >= img.shape[0]-hwid or x_tmp < hwid or y_tmp < hwid or y_tmp>= img.shape[1]-hwid: ##边界条件判断
                        break
                    for i2 in range(-hwid,hwid+1): ##半径宽度使得法线上点四周更多点计数加一
                        for j2 in range(-hwid,hwid+1):
                            img_c[x_tmp+i2][y_tmp+j2] += 1 
    max_num = np.max(img_c)
    print("最多梯度线数为" + str(max_num))
    threshold = max_num*8/10
    for i in range(1, img_c.shape[0]-1):
        for j in range(1, img_c.shape[1]-1):
            img_cc[i][j] = int(img_c[i][j]*255/max_num)
            if img_c[i][j] >= threshold and img_c[i][j]>=img_c[i-1][j] and img_c[i][j]>=img_c[i+1][j] \
            and img_c[i][j] >= img_c[i][j-1] and img_c[i][j] >= img_c[i][j+1]:  ##计数大于阈值并且进行霍夫空间四领域抑制
    #         if img_c[i][j] >= threshold:
    #             img_g[i][j] = img_c[i][j]
                dic[(i,j)] = img_c[i][j]   
#                 cv2.circle(img_g, (j,i), 1, 0, 3)
    #     cv2.imshow('origin', img)
    #     cv2.imshow('canny', canny)
    #     cv2.imshow('test', img_cc)
    #     cv2.imshow('test_origin', img_g)
    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows()
    img_edge = np.zeros(img_g.shape, dtype="uint8")
    print("找到圆心数："+str(len(dic)))
#     min_dist = 10
#     max_dist = min(row, col)//3
    # r_minnum = 10
    centers = sorted(dic.items(), key=lambda x:x[1], reverse=True)
#     r_min = min(row, col)//10
#     r_max = min(row, col)//2
    # center_x = 0
    # center_y = 0
    # num = 0
    # for k in dic.keys():
    #     center_x += k[0]
    #     center_y += k[1]
    #     num += 1
    # center_x = center_x//num
    # center_y = center_y//num

    circles = []
    r_dis = 5
    nums_dis = (r_max-r_min)//r_dis+1
    den = min(row, col)*4

    for center in centers:
        flag_1 = 0
        dic_dis = [[0] for i in range(nums_dis)]
        x = center[0][0]
        y = center[0][1]
        for circle in circles:
            xx = circle[0]
            yy = circle[1]
            dist = (xx-x)**2+(yy-y)**2  
            if dist < (min_dist**2) or dist > (max_dist**2):
                flag_1 = 1
                break      
        if flag_1:
            continue
        for i in range(0, img_g.shape[0]):
            for j in range(0, img_g.shape[1]):
                if canny[i][j]!=0:
                    r = int(round(np.sqrt((i-x)**2+(j-y)**2)))
                    if r >= r_min and r <= r_max:
                        index = (r-r_min)//r_dis
                        dic_dis[index][0] += 1
                        dic_dis[index].append((i,j))
        dic_num = [x[0] for x in dic_dis]
        r_num = max(dic_num)
        loc = dic_num.index(r_num)
        r_in = r_min + r_dis * loc
        r_out = r_in + r_dis
        r_minnum = r_num*8/10
        if r_num <= r_minnum:
            continue
    #     print(r_num)
#         cv2.circle(img, (y,x), r_in, 0, 3)
#         cv2.circle(img, (y,x), r_out, 0, 3)
        circles.append((x,y))
        for edge in dic_dis[loc][1:]:
            img_edge[edge[0]][edge[1]] = 255
    nom = len(np.nonzero(img_edge)[0])
    likelihood = nom/den
    return likelihood
    
    # for circle in circles:
    #     cv2.circle(img, (circle[1], circle[0]), circle[2], 30, 3)

    # for i in range(0, img_g.shape[0]):
    #     for j in range(0, img_g.shape[1]):
    #         if canny[i][j]!=0:
    #             r = int(round(np.sqrt((i-center_x)**2+(j-center_y)**2)))
    #             if r >= r_min and r <= r_max:
    #                 
    # r_in = r_min + r_dis * dic_dis.index(max(dic_dis))
    # r_out = r_in + r_dis

    # cv2.imshow('test_circle', img)
    cv2.imshow('edge', img_edge)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    
if __name__ == "__main__":
    img = cv2.imread('1143.jpg')
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #灰度图
    img_r = img[:,:,2]
    img_g = cv2.GaussianBlur(img_r, (5, 5), 0)
    row = img_g.shape[0]
    col = img_g.shape[1] 
    canny = mycanny(img_g, 30, 60)
    likelihood = myhoughcircle(img_g, canny, min(row, col)//10, min(row, col)//2, 10, min(row, col)//3)
    print("likelihood值为："+str(likelihood))

