def initList():
        dic1 = {"firstName": 'Noah', "lastName": 'M.', "country": 'Switzerland', "continent": 'Amerika', "age": 19,
                "language": 'C', "meal": 'vegetarian'}
        dic2 = {"firstName": 'Anna', "lastName": 'R.', "country": 'Liechtenstein', "continent": 'Europe', "age": 52,
                "language": 'JavaScript', "meal": 'standard'}
        dic3 = {"firstName": 'Ramona', "lastName": 'R.', "country": 'Paraguay', "continent": 'Europe', "age": 29,
                "language": 'Ruby', "meal": 'vegan'}
        dic4 = {"firstName": 'George', "lastName": 'B.', "country": 'England', "continent": 'Europe', "age": 81,
                "language": 'C', "meal": 'vegetarian'}
        ordervarlist1 = [dic1, dic2, dic3, dic4]

        return ordervarlist1


def sortByParam(varList: object, param: str):
        count = {}
        for dic in varList:
                value = dic[param]
                if value in count.keys():
                        count[value] += 1
                else:
                        count[value] = 1
        return count


def main():
        varList = initList()
        count = sortByParam(varList, "continent")

        outList = []
        for i in count:
            print(i)


if __name__ == "__main__":
        main()
