from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Alumno,Genero
from .forms import GeneroForm
from django.contrib.auth.decorators import login_required



# Create your views here.


def base(request):
    return render(request, 'alumnos/base.html')

def index(request):
    return render (request,'alumnos/index.html')

def cartelera(request):
    return render (request,'alumnos/cartelera.html')
def ubicacion(request):
    return render(request,'alumnos/ubicacion.html')

def tienda(request):
    return render(request,'alumnos/tienda.html')

def cinePeliculas(request):
    return render(request,'alumnos/cinePeliculas.html')

def animes(request):
    return render(request,'alumnos/animes.html')

def crud(request):
    alumnos = Alumno.objects.all()
    context={'alumnos':alumnos}
    return render(request,'alumnos/alumnos_list.html',context)


def alumnosAdd(request):
    if request.method is not "POST":
        #NO ES UN POST, POR LO TANTO SE MUESTRA EL FORMULARIO PARA AGREPA.
        generos=Genero.objects.all()
        context={'generos':generos}
        return render(request,'alumnos/alumnos_add.html',context)
    
    else: 
        #ES UN POST POR LO TANTO SE MUESTRA RECUPERAN LOS DATOS DEL FORMULARIO 
        #Y SE GRABAN EN LA TABLA.

        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        aPaterno=request.POST["Paterno"]
        aMaterno=request.POST["Materno"]
        fechaNac=request.POST["fechaNAc"]
        genero=request.POST["genero"]
        telefono = request.POST["telefono"]
        email=request.POST["email"]
        direccion=request.POST["direccion"]
        activo="1"

        objGenero=Genero.objects.get(id_genero = genero)
        obj=Alumno.objects.create(  rut=rut,
                                    nombre=nombre,
                                    apellido_paterno=aPaterno,
                                    apellido_materno=aMaterno,
                                    fecha_nacimiento=fechaNac,
                                    id_genero=objGenero,
                                    telefono=telefono,
                                    email=email,
                                    direccion=direccion,
                                    activo=1 )
        obj.save()
        context={'mensaje':"OK, datos grabados..."}
        return render(request, 'alumnos/alumnos_add.html',context)
    
def alumnos_del(request,pk):
    context={}
    try:
        alumno=Alumno.objects.get(rut=pk)

        alumno.delete()
        mensaje="Bien, datos eliminados..."
        alumnos = Alumno.objects.all()
        context ={'alumnos':alumnos, 'mensajes': mensaje}
        return render(request, 'alumnos/alumnos_list.html',context)
    except:
        mensaje="Error, rut no existe..."
        alumnos = Alumno.objects.all()
        context = {'alumnos': alumnos, 'mensaje': mensaje}
        return render(request, 'alumnos/alumnos_list.html',context)
    
def alumnos_findEdit(request,pk):
    
    if pk != "":
        alumno=Alumno.objects.get(rut=pk)
        generos=Genero.objects.all()

        print(type(alumno.id_genero.genero))

        context={'alumno':alumno,'generos':generos}
        if alumno:
            return render(request, 'alumnos/alumnos_edit.html',context)
        else:
            context={'mensaje':"Error, rut no existe..."}
            return render(request, 'alumnos/alumnos_list.html',context)
        

def alumnosUpdate(request):
    if request.method =="POST":
        #ES UN POST POR LO TANTO SE MUESTRA RECUPERAN LOS DATOS DEL FORMULARIO 
        #Y SE GRABAN EN LA TABLA.

        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        aPaterno=request.POST["paterno"]
        aMaterno=request.POST["materno"]
        fechaNac=request.POST["fechaNAc"]
        genero=request.POST["genero"]
        telefono=request.POST["telefono"]
        email=request.POST["email"]
        direccion=request.POST["direccion"]
        activo="1"

        objGenero=Genero.objects.get(id_genero = genero)

        alumno = Alumno()
        alumno.rut=rut
        alumno.nombre=nombre
        alumno.apellido_paterno=aPaterno
        alumno.apellido_materno=aMaterno
        alumno.fecha_nacimiento=fechaNac
        alumno.id_genero=objGenero
        alumno.telefono=telefono
        alumno.email=email
        alumno.direccion=direccion
        alumno.activo=1
        alumno.save()

        generos=Genero.objects.all()
        context={'mensaje':"OK, datos actualizados...",'generos':generos,'alumno':alumno }
        return render(request, 'alumnos/alumnos_edit.html',context)
    else:
        #NO ES UN POST, POR LO TANTO SE MUESTRA EL FORMULARIO PARA AGREPA.
        alumnos = Alumno.objects.all()
        context={'alumnos':alumnos}
        return render(request, 'alumnos/alumnos_list.html',context)
    















def crud_generos(request):

    generos=Genero.objects.all()
    context ={'generos':generos}
    print("enviando datos generos_list")
    return render(request,"alumnos/generos_list.html",context)

def generosAdd(request):
    print("Estoy en controlador generosAdd...")
    context={}

    if request.method == "POST":
        print("Contralador es un post...")
        form = GeneroForm(request.POST) 
        if form.is_valid:
            print("Estoy en un agrepar, is_valid")
            form.save()

            #LIMPIAR FORM
            form=GeneroForm()

            context={'Mensaje': "OK, datos grabados...","form":form}
            return render(request,"alumnos/generos_add.html",context)
    else:
        form = GeneroForm()
        context={'form':form}
        return render(request, 'alumnos/generos_add.html',context)



def generos_del(request, pk):
    mensajes=[]
    errores=[]
    generos = Genero.objects.all()
    try:
        genero=Genero.objects.get(id_genero=pk)
        context={}
        if  genero:
            genero.delete()
            mensajes.append("Bien, datos eliminar...")
            context = {'genero': generos, 'mensajes':mensajes,'errores':errores}
            return render(request, 'alumnos/generos_list.html',context)
    except:
        print("Error, id no existe...")
        generos=Genero.objects.all()
        mensaje="Error, id no existe"
        context={'mensaje':mensaje,'generos':generos}
        return render(request, 'alumnos/generos_list.html', context)

def generos_edit(request, pk):
    try:
        genero=Genero.objects.get(id_genero=pk)
        context={}
        if genero:
            print("Edit encontro el genero...")
            if request.method =="POST":
                print("edit, es un POST")
                form = GeneroForm(request.POST,isinstance=genero)
                form.save()
                mensaje="Bien, datos actualizados..."
                print(mensaje)
                context = {'genero': genero, 'form':form, 'mensaje':mensaje}
                return render(request, 'alumnos/generos_edit.html',context)
            else:
                #NO SE UN POST
                print("edit, NO es un POST")
                form = GeneroForm(instance=genero)
                mensaje=""
                context = {'genero': genero, 'form': form, 'mensaje': mensaje}
                return render(request, 'alumnos/generos_edit.html',context)
    except:
        print("Error, id no existe...")
        generos=Genero.objects.all()
        mensaje="Error, id no existe"
        context={'mensaje':mensaje, 'generos':generos}
        return render(request, 'alumnos/generos_list.html', context)
    

    