from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection

def metabolism_view(request):
    metabolism = {}
    mname = '%'
    url = ['']
    if request.POST:
        queryRes = []
        mname += request.POST['MetabolismName']
        mname += '%'
    
        with connection.cursor() as cursor:
            query = "select metabolismid, metabolismname, chemicalformula, state, omimid, reference, details from Metabolism natural join Process where metabolismname like %s;"
            
            cursor.execute(query, [mname])
            resp = cursor.fetchall()
            i = 1
            for rows in resp:
                ls = list(rows)
                queryRes.append(ls)
                metabolism[i] = {
                    'MetabolismID': ls[0],
                    'MetabolismName': ls[1],
                    'ChemicalFormula': ls[2],
                    'State': ls[3],
                    'DiseaseName': ls[4],
                    'Reference': ls[5],
                    'Details': ls[6],
                }
                i += 1
    # if request.is_ajax():
    #     if request.GET.get('export') == 'yes':
    #         print(queryRes)
    #     else:
    #         raise Http404

    return render(request, "Metabolism.html", {'metabolism': metabolism})


def disease_view(request):
    gene = {}
    metabolism = {}
    map = {}
    dname = '%'
    url = ['']
    if request.POST:
        queryRes = []
        dname += request.POST['diseasename']
        dname += '%'
        
        with connection.cursor() as cursor:
            query1 = '''
            select omimid,geneid,genename,location,phenotype,details
            from Disease natural join Effect natural join Gene
            where diseasename like %s;
            '''
            cursor.execute(query1, [dname])
            resp = cursor.fetchall()
            i = 1
            for rows in resp:
                ls = list(rows)
                queryRes.append(ls)
                gene[i] = {
                    'Omim_ID': ls[0],
                    'Gene_ID': ls[1],
                    'Gene_name': ls[2],
                    'Location': ls[3],
                    'Phenotype': ls[4],
                    'Details': ls[5],
                }
                i += 1

            query2 = '''
            select metabolismid, metabolismname, chemicalformula, state, reference, details 
            from Metabolism natural join Process 
            where metabolismname like %s;
            '''
            cursor.execute(query2, [dname])
            resp1 = cursor.fetchall()
            j = 1
            for rows in resp1:
                ls = list(rows)
                queryRes.append(ls)
                metabolism[j] = {
                    'MetabolismID': ls[0],
                    'Metabolism_Name': ls[1],
                    'Formula': ls[2],
                    'State': ls[3],
                    'Reference': ls[4],
                    'Details': ls[5],
                }
                j += 1

            query3 = '''
            select diseasename, mapimage,mapid
            from Map
            where diseasename like %s;
            '''
            cursor.execute(query3, [dname])
            resp2 = cursor.fetchall()
            k = 1
            for rows in resp2:
                ls = list(rows)
                queryRes.append(ls)
                map[j] = {
                    'diseasename': ls[0],
                    'picture': ls[1],
                    'kegg': ls[2],
                }
                k += 1
    
    return render(request, "Disease.html", {'gene': gene, 'metabolism': metabolism, 'map': map})    

def tutorial_view(request):
    return render(request, "Tutorial.html")

def about_view(request):
    return render(request, "About.html")

def home_view(request):
    return render(request, "Home.html")

def cytoscape_view(request):
    return render(request, "kenan.html")