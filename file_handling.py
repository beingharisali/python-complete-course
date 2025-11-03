company_info = open('data.txt', 'w')
# print(company_info.readable()) # readable() - will return True of False is file is readable or not
# print(company_info.read()) # read() - will return whole data existing in file
# print(company_info.readline()) # readline() - will only read first element
# print(company_info.readlines()[4]) # readlines() - will read all data in file and convert in array
# for team in company_info.readlines():
#     print(team)
company_info.write('\nElina - Quality Assurance')
company_info.close()


# Haris Ali - Founder (Heapware)
# Project Manager - Muhammad Ali
# Frontend Team - 10
# Frontend Team Lead - Shahzaib
# Backend Team - 5
# Backend Team Lead - Sehar
# Client - Juliya Pasternack - New York
# Client - Marina Roque - United Kingdom
# Elina - Quality Assurance
# Elina - Quality Assurance
# Elina - Quality Assurance