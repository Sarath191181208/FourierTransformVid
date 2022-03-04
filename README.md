[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/Sarath191181208/FourierTransformVid/index.html)

# Fourier transform

Fourier transform a function that converts the function of time to function of frequency. This project uses Fourier transform to darw the svg's using the epicycles.
$\displaystyle{X*k = \sum*{n=0}^{N-1} x_n \cdot e^{-i 2 \pi k n / N}}$

# Description

Works on a basic priciple of Fourier transform. We store the svg's in index.html as a svg element and it's property is set to hidden so it's not visible. We are using the fourier transform to convert our svg points into epicycles.

## Demo

![Image](https://github.com/Sarath191181208/FourierTransformVid/blob/master/images/Screenshot.png)

## Run Locally

Clone the project

```bash
  git clone https://github.com/Sarath191181208/FourierTransformVid
```

Go to the project directory

```bash
  cd ./FourierTransformVid
```

Install dependencies

```bash
  pip3 install -r requirements.txt
```

You need to install Latex on your machine too. And don't forget to add it to path too.
[Install Latex](https://miktex.org/download)

Run the project Locally

```bash
  manim animations/main.py -pqm CreateCircle
```

## References

WikiPedia : https://en.wikipedia.org/wiki/Fourier_transform

3B1B : https://www.youtube.com/watch?v=r6sGWTCMz2k&vl=en

Coding train Fourier series : https://www.youtube.com/watch?v=Mm2eYfj0SgA

Better explained: https://betterexplained.com/articles/an-interactive-guide-to-the-fourier-transform/

## Requirements

- python `Make sure to add to path`
- manim `pip install manim`
- scipy `pip install scipy`
- numpy `pip install numpy`
