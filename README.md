# yt-downloader!
DEPI Final Project: Automated Deployment Pipeline with Jenkins and Docker

Week 1: Initial Setup & Planning
 Task 1 : Install Jenkins and Docker: Set up the Jenkins server and Docker on local Enviroment
![image](https://github.com/user-attachments/assets/3f5badc1-567a-4e27-9c3b-7148c6cd2acd)
![image](https://github.com/user-attachments/assets/d0571f91-32b0-44e6-80f2-8857a6f15688)
![image](https://github.com/user-attachments/assets/a9c35085-7fb1-4b6a-9056-242b97fa3122)
![image](https://github.com/user-attachments/assets/94948884-a84f-4b98-94e1-e143202196bc)
![image](https://github.com/user-attachments/assets/0d782f6f-f2d2-4ad5-8658-94e57a993755)

Task2: Set up Ansible: Install Ansible for configuration management

-	Controller Node
  
![image](https://github.com/user-attachments/assets/10f2d07f-a99d-4a98-a915-adfc533e612c)

-	Host
  
![image](https://github.com/user-attachments/assets/919d3cad-2603-43a7-ab78-c08dd2905814)
![image](https://github.com/user-attachments/assets/83599f29-c498-4802-9ac0-aa403b14ffa4)
![image](https://github.com/user-attachments/assets/d0e17042-a0f5-40c0-a1da-8f8b477efe1b)

Task3: Create the containerized application

-	The idea of application is a web-based tool that allows users to download YouTube videos by simply entering a video URL and fetch the video with the best resolution and store it inside mounted volume inside container
  
-	App Python script
  
![Annotation 2025-02-17 024354](https://github.com/user-attachments/assets/01e9167e-6d1c-4048-b500-e4a024a1c3da)
![Annotation 2025-02-17 024457](https://github.com/user-attachments/assets/860cd9f2-6d39-4a32-baa3-9da774989fa5)

-	Dockerfile
-	
![Annotation 2025-02-17 024518](https://github.com/user-attachments/assets/870a15eb-91fd-45e2-9294-88624879af92)

-	Building the docker image
  
![Annotation 2025-02-16 002030](https://github.com/user-attachments/assets/3cfb82bb-bdd3-44b2-b2d9-c269e29d9d87)

-	Creating the application container
  
![Annotation 2025-02-16 003534](https://github.com/user-attachments/assets/b86af7fc-819f-495c-aff6-5174196c7154)

-	Browsing the application and making download for video
  
![Ubuntu (2)-2025-02-16-00-21-40](https://github.com/user-attachments/assets/37c9321d-3613-4f7f-bb36-77ba87caff46)
![Ubuntu (2)-2025-02-16-00-23-48](https://github.com/user-attachments/assets/559b4ada-101e-472d-bb6f-413697b6b80b)


Week 2: Jenkins & CI Integration

Task1: Create Jenkins Jobs: Configure Jenkins to build the Dockerized application.

 - Configure 2 piplines for build docker image and run docker container

![Ubuntu (2)-2025-02-18-06-25-00](https://github.com/user-attachments/assets/4c2776f7-c295-4b02-9724-0b6cbfa6c4ef)
![Ubuntu (2)-2025-03-07-05-46-34](https://github.com/user-attachments/assets/67e91ef8-9a34-4720-a11c-e1c0d8b3fea0)
.![Ubuntu (2)-2025-02-18-06-12-08](https://github.com/user-attachments/assets/08f4942b-bbef-4098-87e6-fed559c954d1)
![Ubuntu (2)-2025-03-07-05-45-11](https://github.com/user-attachments/assets/66b95c16-ef81-44cd-8c8e-f0c23b71704a)
![Ubuntu (2)-2025-02-19-05-30-13](https://github.com/user-attachments/assets/32296b7e-3762-4e92-b19d-6d34cf631368)

- checking image & container
![2](https://github.com/user-attachments/assets/54414ec0-9054-40de-965b-0382320c2935)
![Ubuntu (2)-2025-02-19-06-19-41](https://github.com/user-attachments/assets/aa280390-cf4f-4065-b024-8dc7436e2b2f)
![Ubuntu (2)-2025-03-05-05-34-11](https://github.com/user-attachments/assets/f0db1c62-dd7c-45d8-83e5-530a9487437f)

- Browsing the application
  ![Ubuntu (2)-2025-02-19-06-20-05](https://github.com/user-attachments/assets/076d36a2-66f0-47c8-a30f-c22013907afb)

  - Kubernetes Integration: configure Kubernetes to orchestrate the
    deployment of Docker containers.
    
    ![Ubuntu (2)-2025-03-07-05-04-28](https://github.com/user-attachments/assets/8df7a61f-a15b-4f64-bee2-f9e65e25a25a)
    ![ci_cd Plpeline - Youtube downloader drawio(2)](https://github.com/user-attachments/assets/869fb94a-2bd4-4585-93ae-0d0c12c2a8e9)


    


