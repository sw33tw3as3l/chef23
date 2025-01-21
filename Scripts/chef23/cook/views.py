from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import GraphProject
from django.contrib.auth.models import User

import jsonpickle


@login_required(login_url='/api-auth/login')
def home(req):
    if req.method == 'POST':
        new_project = GraphProject(owner=req.user, project_name=req.POST['project_name'],
                                   vertex="1-2-", edge="1~2-")
        
        new_project.save()
        st = '/cook/'+str(req.POST['project_name'])+''
        print("here11111111111")
        print(st)
        return redirect(st)
    return render(req, 'home.html')

@login_required(login_url='/api-auth/login')
def graph(req, project_name):
    gr = GraphProject.objects.all()
    gr = gr.filter(owner=req.user).filter(project_name=project_name)
    
    return render(req, 'graph.html', context={
        "vertex" : gr[0].vertex,
        "edge": gr[0].edge,
        "project_name": project_name,
    })


@login_required(login_url='/api-auth/login')
def add_vertex(req, project_name):
    gr = GraphProject.objects.all()
    gr = gr.filter(owner=req.user).filter(project_name=project_name)[0]
    gr.vertex = gr.vertex + req.POST['id'] + '-'
    gr.save()
    
    return redirect('/cook/'+project_name)

@login_required(login_url='/api-auth/login')
def add_edge(req, project_name):

    gr = GraphProject.objects.all()
    gr = gr.filter(owner=req.user).filter(project_name=project_name)[0]
    gr.edge = gr.edge + req.POST['from'] + '~' + req.POST['to'] + '-'
    gr.save()
    
    return redirect('/cook/'+project_name)