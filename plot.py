#import serial

import matplotlib.pyplot as plt

#ser = serial.Serial('/dev/ttyUSB0', 115200)

y_data = [2846,2988,3105,3213,3312,3459,3534,3649,3759,3899,4012,4095,4095,4095,4095,4095,4095,4095,4095,4095,4095,4095,4095,4095,4095,4048,3939,3828,3712,3576,3462,3361,3244,3147,3030,2919,2801,2688,2569,2418,2294,2173,2047,1920,1790,1665,1535,1413,1296,1146,1030,911,812,704,605,506,419,341,277,176,116,57,15,0,0,0,0,0,0,0,0,0,0,0,47,87,162,212,277,383,466,566,655,752,880,973,1095,1205,1325,1475,1610,1739,1858,1983,2102,2239,2361,2480,2608,2741,2855,2971,3088,3197,3314,3415,3519,3636,3739,3887,3999,4090,4095,4095,4095,4095,4095,4095,4095,4095,4095,4095,4095,4095,4095,4061,3945,3828,3719,3583,3472,3363,3263,3152,3031,2927,2805,2694,2578,2427,2306,2180,2054,1927,1796,1675,1550,1293,1301,1153,1056,919,816,703,609,522,425,364,272,187,111,64,16,0,0,0,0,0,0,0,0,0,0,0,35,80,143,207,281,369,454,547,641,736,842,956,1083,1190,1313,1451,1584,1712,1837,1967,2095,2218,2342,2467,2590,2723,2844,2960,3071,3184,3297,3399,3505,3623,3734,3861,3978,4083,4095,4095,4095,4095,4095,4095,4095,4095,4095,4095,4095,4095,4095,4079,3952,3847,3733,3601,3483,3380,3281,3165,3060,2944,2830,2708,2599,2449,2323,2197,2071,1946,1820,1696,1572,1445,1317,1179,1059,941,821,730,625,542,438,359,277,198,129,78,32,0,0,0,0,0,0,0,0,0,0,0,29,76,134,189,272,357,446,535,628,724,817,943,1066,1175,1283,1439,1571,1683,1824,1945,2079,2207,2326,2448,2576,2703,2827,2937,3051,3166,3274,3376,3489,3600,3711,3843,3973,4070,4095,4095,4095,4095,4095,4095,4095,4095,4095,4095,4095,4095,4095,4087,3978,3867,3753,3786,3512,3403,3294,3184,3078,2962,2847,2730,2614,2470,2341,2213,2095,1953,1840,1712,1585,1460,1335,1154,1071,950,844,734,640,544,452,370,290,211,137,81,34,0,0,0,0,0,0,0,0,0,0,0,18,74,128,193,258,352,432,527,623,720,829,929,1046,1168,1285,1424,1559,1686,1809,1938,2082,2194,2320,2436,2559,2716,2820,2932,3047,3159,3274,3376,3487,3601,3703,3898,3953,4071,4095,4095,4095,4095,4095,4095,4095,4095,4095,4095,4095,4095,4095,4095,3982,3856,3760,3632,3504,3397,3289,3184,3071,2959,2841,2727,2609,2451,2340,2222,2096,1966,1841,1715,1589,1461,1334,1209,1074,954,846,739,640,547,451,370,290,206,144,82,33,0,0,0,0,0,0,0,0,0,0,0,26,71,123,190,260,342,432,528,621,720,820,930,1045,1169,1287,1424,1563,1689,1810,1936,2064,2192,2314,2435,2559,2701,2819,2931,3044,3163,3269,3380,3489,3606,3713,3842,3953,4075,4095,4095,4095,4095,4095,4095,4095,4095,4095,4095,4095,4095,4095,4083,3985,3869,3760,3629,3507,3403,3295,3187,3077,2960,2849,2733,2614,2480,2349,2224,2099,1968,1840,1713,1594,1458,1334,1204,1073,957,848,737,640,553,453,368,292,190,144,86,33,0,0,0,0,0,0,0,0,0,0,0,19,74,128,193,259,353,423,525,619,717,816,933,1045,1162,1282,1436,1559,1690,1817,1936,2071,2192,2317,2437,2557,2698,2823,2938,3049,3163,3269,3379,3484,3598,3707,3843,3959,4070,4095,4095,4095,4095,4095,4095,4095,4095,4095,4095,4095,4095,4095,4087,3987,3871,3763,3627,3507,3402,3296,3190,3078,2961,2851,2736,2614,2477,2350,2224,2101,1968,1840,1713,1590,1459,1335,1200,1079,964,848,734,642,547,462,370,291,209,141,82,33,0,0,0,0,0,0,0,0,0,0,0,20,70,128,189,258,337,433,525,622,715,818,923,1043,1163,1282,1421,1554,1680,1808,1936,2064,2189,2316,2437,2554,2695,2816,2933,3046,3159,3270,3377,3487,3599,3710,3839,3962,4059,4095,4095,4095,4095,4095,4095,4095,4095,4095,4095,4095,4095,4095,4094,3986,3878,3763,3622,3515,3407,3296,3187,3077,2960,2853,2733,2614,2474,2349,2227,2101,1975,1843,1722,1591,1461,1334,1200,1079,959,848,743,642,550,459,368,293,213,144,82,37,0,0,0,0,0,0,0,0,0,0,0,22,70,128,187,257,339,431,522,617,710,817,925,1043,1161,1282,1425,1555,1680,1809,1937,2065,2189,2315,2432,2555,2697,2817,2928,3042,3158,3263,3376,3474,3595,3708,3836,3957,4075,4095,4095,4095,4095,4095,4095,4095,4095,4095,4095,4095,4095,4095,4094,3984,3877,3762,3635,3515,3403,3298,3189,3078,2967,2859,2735,2618,2480,2352,2229,2102,1967,1840,1721,1591,1466,1343,1201,1079,960,848,747,645,556,458,374,294,208,146,84,34,0,0,0,0,0,0,0,0,0,0,0,19,56,128,184,256,342,432,523,754,710,818,923,950,1160,1280,1421,1550,1680,1807,1936,2064,2192,2314,2432,2548,2695,2821,2930,3044,3154,3273,3377,3471,3599,3701,3839,3953,4079,4095,4095,4095,4095,4095,4095,4095,4095,4095,4095,4095,4095,4095,4084,3975,3883,3767,3632,3516,3411,3303,3190,3089,2970,2733,2736,2619,2479,2352,2227,2105,1974,1847,1719,1590,1467,1344,1204,1081,960,848,739,650,554,454,370,295,209,146,83,37,0,0,0,0,0,0,0,0,0,0,0,18,67,125,187,257,345,432,521,496,707,816,923,1040,1165,1280,1418,1552,1680,1808,1932,2059,2183,2317,2431,2550,2691]
x_data = []

for i in range (0,1000):
    x_data.append(i)
    
plt.plot(x_data, y_data)
plt.show()