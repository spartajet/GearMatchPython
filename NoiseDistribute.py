__author__ = 'Xiaozhong GUO'
import os
import numpy as np
import matplotlib.pyplot as plt


noisePath = "/Volumes/MYSD/项目/汽车齿轮高效配对/E04.参考资料/实验数据/数据及说明/12组特征齿轮试验/特征齿轮实验振动噪声数据/"

drivingXs = []
drivingYs = []
drivingZs = []
drivedXs = []
drivedYs = []
drivedZs = []
Noises = []
fileList = os.listdir(noisePath)
for i in range(0, len(fileList)):
    filePath = os.path.join(noisePath, fileList[i])
    if os.path.isfile(filePath) and filePath.endswith(".TXT"):
        data = np.loadtxt(filePath, delimiter='\t')
        drivingX = data[:, 2]
        drivingXs.append(drivingX.ptp())
        drivingY = data[:, 3]
        drivingYs.append(drivingY.ptp())
        drivingZ = data[:, 4]
        drivingZs.append(drivingZ.ptp())
        drivedX = data[:, 5]
        drivedXs.append(drivedX.ptp())
        drivedY = data[:, 6]
        drivedYs.append(drivedY.ptp())
        drivedZ = data[:, 7]
        drivedZs.append(drivedZ.ptp())
        noise = data[:, 8]
        Noises.append(noise.ptp())

noise_10 = []
noise_30 = []
noise_60 = []
noise_90 = []
noise_120 = []

for i in range(0, len(Noises)):
    if i % 5 == 0:
        noise_10.append(Noises[i])
    elif i % 5 == 1:
        noise_30.append(Noises[i])
    elif i % 5 == 2:
        noise_60.append(Noises[i])
    elif i % 5 == 3:
        noise_90.append(Noises[i])
    elif i % 5 == 4:
        noise_120.append(Noises[i])

X = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
plt.plot(X, noise_10, label="noise_10")
plt.plot(X, noise_30, label="noise_30")
plt.plot(X, noise_60, label="noise_60")
plt.plot(X, noise_90, label="noise_90")
plt.plot(X, noise_120, label="noise_120")

plt.legend(loc='best')
plt.xlabel("group")
plt.ylabel("noise")
plt.show()
plt.savefig("noise.jpg")

# plt.hist(drivingXs, bins=20)
# plt.xlabel("Distribute")
# plt.ylabel("Driving X")
# plt.show()
#
# plt.hist(drivingYs, bins=20)
# plt.xlabel("Distribute")
# plt.ylabel("Driving Y")
# plt.show()
#
# plt.hist(drivingZs, bins=20)
# plt.xlabel("Distribute")
# plt.ylabel("DrivingZ")
# plt.show()
#
# plt.hist(drivedXs, bins=20)
# plt.xlabel("Distribute")
# plt.ylabel("Drived X")
# plt.show()
#
# plt.hist(drivedYs, bins=20)
# plt.xlabel("Distribute")
# plt.ylabel("Drived Y")
# plt.show()
# plt.hist(drivedZs, bins=20)
# plt.xlabel("Distribute")
# plt.ylabel("Drived Z")
# plt.show()
#
# plt.hist(Noises, bins=20)
# plt.xlabel("Distribute")
# plt.ylabel("Noise")
# plt.show()
