from time import time
# Explore acceptable input sizes for each common runtime

# const 10000000 0
def constant(n):
    s = time()
    print 'const\t' + str(time() - s)


# log(n)	1	2.71797180176e-05
# log(n)	10	1.38282775879e-05
# log(n)	100	1.4066696167e-05
# log(n)	1k	3.09944152832e-05
# log(n)	10k	0.000133991241455
# log(n)	100k	0.00118207931519
# log(n)	1m	0.0124118328094
# log(n)	10m	0.0942230224609
# log(n)	100m	0.807785987854
# log(n)	1b	7.47305512428  ... slowish
# too slow for bigger n (n = 10b takes 88.7487230301)
def log_n(n):
    s = time()
    for i in xrange(int(n ** 1/2)):
        pass
    print 'log(n)\t' + str(n) + '\t' + str(time()-s)


# n	1	2.00271606445e-05
# n	10	9.05990600586e-06
# n	100	1.38282775879e-05
# n	1k	3.91006469727e-05
# n	10k	0.000272989273071
# n	100k	0.00219202041626
# n	1m	0.0212440490723
# n	10m	0.163300037384
# n	100m	1.50400400162
# too slow for bigger n (n = 1b takes 16.4811339378s)
def linear(n):
    s = time()
    for i in xrange(n):
        pass
    print 'n\t' + str(n) + '\t' + str(time()-s)


# n*log(n)	1	5.00679016113e-06
# n*log(n)	10	2.14576721191e-06
# n*log(n)	100	7.39097595215e-05
# n*log(n)	1k	0.00986790657043
# n*log(n)	10k	0.814930915833
# too slow for bigger n (n = 100k takes 79.7037620544s)
def n_log_n(n):
    s = time()
    for i in xrange(n * int(n ** 1/2)):
        pass
    print 'n*log(n)\t' + str(n) + '\t' + str(time()-s)


# n**2	1	1.59740447998e-05
# n**2	10	1.38282775879e-05
# n**2	100	0.000188112258911
# n**2	1k	0.020977973938
# n**2	10k	1.5981669426
# too slow for bigger n
def n_2(n):
    s = time()
    for i in xrange(n**2):
        pass
    print 'n**2\t' + str(n) + '\t' + str(time()-s)


# n**3	1	5.96046447754e-06
# n**3	10	2.50339508057e-05
# n**3	100	0.0282590389252
# too slow for bigger n (n = 1k takes 16.0581169128)
def n_3(n):
    s = time()
    for i in xrange(n**3):
        pass
    print 'n**3\t' + str(n) + '\t' + str(time()-s)


# 2**n	1	4.05311584473e-06
# 2**n	10	1.69277191162e-05
# 2**n	25	0.539837837219
# too slow for bigger n (n = 30 takes 19.0504479408s)
def _2_n(n):
    s = time()
    for i in xrange(2**n):
        pass
    print '2**n\t' + str(n) + '\t' + str(time()-s)


# n**n	1	1.90734863281e-06
# n**n	3	1.90734863281e-06
# n**n	5	8.20159912109e-05
# n**n	8	0.281722784042
# too slow for bigger n (n = 10 takes 160.258363008s)
def n_n(n):
    s = time()
    for i in xrange(n**n):
        pass
    print 'n**n\t' + str(n) + '\t' + str(time()-s)


log_n(1e10)
