from collections import Counter

tickets = ['Kazan - Moscow', 'SPb - kazan', 'kazan - japan']
res = []

def search_tickets(tickets):

    for city in tickets:
        city = city.lower().split()

        for count in city:
            if '-' not in count:
                res.append(count)
            a = list(Counter(res).values())
    if a[0] % 2 == 0:
        return True
    else:
        return False
            
        
       