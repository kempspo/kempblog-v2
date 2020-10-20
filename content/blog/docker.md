Title: Containers and why I love them
Date: 2020-10-20 00:00
Category: Blog
Tags: Docker, Best practices, Containers
Slug: contiainers-and-why-i-love-it
Authors: Kemp Po
Summary: 

Every developer has probably encountered this:
> "It worked on my machine". 

Fear not! We already have a the solution to this problem and they're called
containers. No, not the enormous amount of plastic every asian mom keeps 
somewhere in the kitchen.

### What are containers?
They're meant to package up and hold the code and its dependencies like how the
plastic ones hold your food, instead of you holding it in your hands. It enables
you run your applications reliably and easily in different environments. 
Containers are lightweight, standalone, executable packages of software that 
contains everything needed to run the programs you've created. Containers even
have their own filesystems!

These containers have to be created somehow through these blueprints, which we
call **images**. Images are essentially schematics that define a filesystem, 
the code or binary, runtimes, dependencies, and any other thing required to run
the code. Without an image, there is no container. 

Now that we know what containers are,
### Why containers?
We actually have different options of solving the problem, so lets weigh one of
the largest contenders to containers, the Virtual Machines or VMs. Virtual 
Machines originally started off because servers processing power increased and
normal applications aren't able to maximize these resources. This, however,
introduced a new issue, portability.

Some key differences between containers and virtual machines are:

| Features | Containers | Virtual Machines |
| -------- | ---------- | ---------------- |
| Operating System | Runs just a portion of an OS, uses less system resources and can be tailored to what is needed | Runs a complete OS, including the kernel, thus using up more system resources |
| Guest Compatibility | Needs to run the same OS verion as the host | Runs almost any OS |
| OS Updates | All you need to do is update the image build file, rebuild the image and redeploy | You will need to update every VM instance or recreate them |



Containers vs VMs


What is Docker?
How to Docker?
Teaser to Kubernetes