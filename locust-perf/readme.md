# Grafana integration with locust using prometheus
 
## Documentation
There are two yaml files in this directory  

    - one to configure and deploy the whole setup including locust 
    - one to configure prometheus

I've intentionally left the locustfile.py along with requirements.txt blank, since each application is different and the requests should be handcrafted for each case.

Feel free to use it, comment on it and let me know if there's an issue with the script. 

* Do not specify containerName for worker, doing so might prevent the worker from being scaled. 



## Command Line

```bash
  docker-compose --build up -d --scale workers=4 
```
    
## Authors

- [@iAmPraveena](https://www.github.com/iAmPraveena)


## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## 🚀 About Me
From from my LinkedIN: 


IT Professional with 12 years of experience has honed my craft as a QA Automation Engineer, but I'm more than just a scriptwriter. I'm an innovator and problem solver, leveraging the power of Python and Robot Framework to tackle complex testing challenges in diverse domains like healthcare, big data, media, and analytics.

Here's what sets me apart:

Innovation in Automation: I don't settle for generic scripts. I conceive and implement creative automation solutions that address unique industry needs. Think automating compliance checks in healthcare apps, building custom performance benchmarks for Big Data pipelines, or even using AI-powered tools to automate visual regression testing.
Problem-Solving Prowess: When roadblocks arise, I don't panic. I draw on my extensive experience and technical expertise to devise unconventional solutions, ensuring efficient and effective testing even in challenging environments.
Python and Robot Mastery: I'm not just proficient in these tools, I push their boundaries. I write elegant and efficient Python code for robust frameworks, and leverage Robot Framework's flexibility to create self-documenting, maintainable test scripts that empower collaboration.

I'm not just a QA Automation Engineer. I'm a strategic thinker, a creative problem solver, and a technology enthusiast driven by a passion for quality. I'm confident that my innovative approach and technical expertise can be a game-changer for your team.

