---
layout: page
subtitle: Exercices d'entraînement
mathjax: true
---

Étudier les variations et la convexité de la fonction \\(f\\) définie sur \\(\mathbb{R}\\) par \\(f(x)=x e^{x^2}\\).


<details><summary>Solution</summary>

On détermine les limites de \(f\) aux bornes de son ensemble de définition par composées et produits de foncitons usuelles. On obtient :

$$\lim_{x \to -\infty} f(x)=-\infty \text{et} \lim_{x \to +\infty} f(x)=+\infty $$.

D'autre part la fonction \(f\) est dérivable sur \(\mathbb{R}\) comme produit et composée de fonctions dérivables sur \(\mathbb{R}\) et, pour tout réel \(x\), on a :

$$f'(x)=e^{x^2}(2x^2+1).$$

Puisque pour tout \(x \in \mathbb{R}\) on a \(e^{x^2} >0\) et \(2x^2+1 >0\), on en déduit le signe de \(f'(x)\) et les variations de \(f\) sur \(\mathbb{R}\) :


<center><IMG src="/assets/img/var_ex1.png"  alt="Var.png"/></center>


On détermine la convexité de \(f\) en étudiant le signe de sa dérivée seconde \(f''\). La fonction \(f\) est deux fois dérivable et pour tout réel \(x\), on a :

$$f''(x)=2x(2x^2+3)\e^{x^2}.$$

Le signe de \(f''(x)\) sur \(\mathbb{R}\) étant déterminé par celui de \(2x\), on en déduit son tableau de signes :


<center><IMG src="/assets/img/ex1_2.png"  alt="Conv.png"/></center>


Finalement la fonction \(f\) est concave sur \(]-\infty ; 0[\) et convexe sur \(]0;+\infty[\). La courbe représentative de \(f\) admet un point d'inflexion en son point d'abscisse 0.
</details>


