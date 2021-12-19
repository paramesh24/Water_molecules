import numpy as np
nmolecule =50
system_size=60
separation=2

def check(c,pos,se):
  re=True 
  for j in range(0,len(pos)):
    mgv=pos[j]-c
    if abs(mgv[0])<se and abs(mgv[1])<se and abs(mgv[2])<se:
        re=False
        break           
  return re





atoms=np.array([[0,0,0], 
               [0.9584,0,0],
               [-0.23996,0.92787,0]])

position=[]
types=[]
char=[]
mole=[]

n=1
while n<=nmolecule:
    cor=np.array([np.random.uniform(1,system_size-1),np.random.uniform(1,system_size-1),0])
    t=1
    if n==1:
        for atom in atoms:
            position.append(cor+atom)
            if t==1:
                types.append(1)
                char.append(-1.1794)
                mole.append(n)
            else:
                types.append(2) 
                char.append(0.5897)
                mole.append(n)
            t+=1
        n+=1  
        
    else:
      if check(cor,position,separation)==True:     
         for atom in atoms:
              position.append(cor+atom)
              if t==1:
                 types.append(1)
                 char.append(-1.1794)
                 mole.append(n)
              else:
                types.append(2) 
                char.append(0.5897)
                mole.append(n)
              t+=1
         n+=1        
                     
with open('rand.data','w') as fdata:
    fdata.write("#Random atom data\n\n")
    fdata.write("{} atoms\n".format(len(position)))   
    fdata.write("{} bonds\n".format(int(len(mole)/3)*2)) 
    fdata.write("{} angles\n\n".format(int(len(mole)/3)))                      
    fdata.write("{} atom types\n".format(2)) 
    fdata.write("{} bond types\n".format(1)) 
    fdata.write("{} angle types\n\n".format(1))     
    #Box dimension
    fdata.write("{} {} xlo xhi\n".format(0.0 ,system_size ))  
    fdata.write("{} {} ylo yhi\n".format(0.0 ,system_size ))  
    fdata.write("{} {} zlo zhi\n\n".format(-0.2,0.2))  
    fdata.write("Atoms\n\n")
    for i in range(0,len(position)):
        fdata.write("{}  {}  {}  {}  {}   {}   {}\n".format(i+1,mole[i],types[i],char[i],position[i][0],position[i][1],position[i][2]))

    fdata.write("\n")        
    fdata.write("Bonds\n\n") 
    n=0       
    for i in range(0,len(position),3):
        n+=1
        fdata.write("{}  1  {}  {} \n".format(n,i+1,i+2) ) 
        n+=1
        fdata.write("{}  1  {}  {} \n".format(n,i+1,i+3) ) 

    fdata.write("\n")        
    fdata.write("Angles\n\n")
    
    n=0       
    for i in range(0,len(position),3):
        n+=1
        fdata.write("{}  1  {}  {}  {}\n".format(n,i+2,i+1,i+3) )    

