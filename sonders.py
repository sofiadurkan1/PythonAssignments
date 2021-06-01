# my_list = [1,2,3]
# for i in my_list :
#     for j in my_list:
#         for k in my_list:
#             if i !=j and j !=k and i !=k :
#                 print(i,j,k)

# my_list = [1,2,3]
# [[i,j,k] for i in my_list for j in my_list for k in my_list if i !=j and j !=k and i !=k]
# print(list(my_list))



# liste = [1, 2, 3]
# result1= []
# perm = 1  
# # perm: başlangıçta liste tek elemanlı bile olsa 1 olasılık vardır.
# for i in range(1, len(liste)+1):
#     perm = i * perm  
# # perm : toplam kaç farklı şekilde olabileceğine ilişkin sayı.
# per = int(perm * 0.5)  
# # per: toplam değişik listelerin yarısı diğer yarısının tersi olarak yer almaktadır. 
# # o yüzden diğer yarısını en son ekleyeceğim. 
# for i in range(per):
# # []: toplam değişik listelerin yarısı kadar boş liste ekledim.
#     result1.append([])
# for i in range(len(liste)):
#                for j in result1:
#                     j.append(0) 
# # [x, x, x, x....]üzerinde rahat çalışmak için, 
# # her bir değişik listeye listedeki toplam eleman kadar boş bir değer atadım. 
# k = 0
# for i in liste: 
# # bu bölümde tüm listelere birer kaydırararak başlangıçtaki liste elemanlarımı ekledim.  
#     k += 1
#     for j in range(per):
#         if k < len(liste):
#             result1[j][k] = i
#             k += 1
#         else:
#             k = 0
#             result1[j][k] = i
#             k += 1
# result2 = []
# for i in result1: 
# # tüm listelerin bir de tersini alıyorum
#     result2.append(i[::-1])
# result = result2 + result1 
# # tersini (perm/2 adet) , düzünü (perm/2 adet) topluyorum.)
# print(len(result), result, sep = "\n")


# data = [1, 2, 3]
# desired = [
#     [x, y, z]
#     for x in data
#     for y in data
#     for z in data
#     if (x != y and y != z and x != z)
#     ]
# print(desired)


from typing import Iterator


num = [1,2,3]
num_set = set(num)
print(num)

# for index in range(len(num)):
#     [body for i in iterator]


for i in range(3):
    print("bugun ayrilik gunu")


solution = [[]]
num = [1,2,3]  # bu listenin permütasyonunu (her ihtimalini) yazdırmamız isteniyor
num_set = set(num)
for index in range(len(num)) :  # num eleman sayısı kadar iterate et (yani 3 kere)
  solution = [i + [j] for i in solution for j in num_set.difference(set(i))]  
  print(solution)  # her iterasyon çıktısı
solution   # istenen sonuç




equall = lambda x,y,z: [x,y,z].count(max([x,y,z], key=[x,y,z].count)) \
          if [x,y,z].count(max([x,y,z], key=[x,y,z].count)) > 1 else 0
