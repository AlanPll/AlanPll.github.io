---
layout: page
subtitle: Exercices d'entraînement
mathjax: true
---

Étudier les variations et la convexité de la fonction définie sur \\(\mathbb{R}\\) par \\(f(x)=x e^{x^2}\\).
<details><summary>Solution</summary>

La fonction \(f\) est dérivable sur \(\mathbb{R}\) comme produit et composée de fonctions dérivables sur \(\mathbb{R}\) et, pour tout réel \(x\), on a :

$$f'(x)=e^{x^2}(2x^2+1).$$

$$
\begin{center}
\begin{tikzpicture}[scale=0.875]
% Styles 
\tikzstyle{cadre}=[thin]
\tikzstyle{fleche}=[->,>=latex,thin]
\tikzstyle{nondefini}=[lightgray]
% Dimensions Modifiables
\def\Lrg{1.5}
\def\HtX{1}
\def\HtY{0.5}
% Dimensions Calculées
\def\lignex{-0.5*\HtX}
\def\lignef{-1.5*\HtX}
\def\separateur{-0.5*\Lrg}
% Largeur du tableau
\def\gauche{-1.5*\Lrg}
\def\droite{4.5*\Lrg}
% Hauteur du tableau
\def\haut{0.5*\HtX}
\def\bas{-2.5*\HtX-2*\HtY}
% Ligne de l'abscisse : x
\node at (-1*\Lrg,0) {$x$};
\node at (0*\Lrg,0) {$-\infty$};
\node at (2*\Lrg,0) {$$};
\node at (4*\Lrg,0) {$+\infty$};
% Ligne de la dérivée : f'(x)
\node at (-1*\Lrg,-1*\HtX) {$f'(x)$};
\node at (0*\Lrg,-1*\HtX) {$$};
\node at (1*\Lrg,-1*\HtX) {$+$};
\node at (2*\Lrg,-1*\HtX) {$$};
\node at (4*\Lrg,-1*\HtX) {$$};
% Ligne de la fonction : f(x)
\node  at (-1*\Lrg,{-2*\HtX+(-1)*\HtY}) {$f(x)$};
\node (f1) at (0*\Lrg,{-2*\HtX+(-2)*\HtY}) {$$};
\node (f2) at (2*\Lrg,{-2*\HtX+(0)*\HtY}) {$$};
\node (f3) at (4*\Lrg,{-2*\HtX+(0)*\HtY}) {$$};
% Flèches
\draw[fleche] (f1) -- (f2);
% Encadrement
\draw[cadre] (\separateur,\haut) -- (\separateur,\bas);
\draw[cadre] (\gauche,\haut) rectangle  (\droite,\bas);
\draw[cadre] (\gauche,\lignex) -- (\droite,\lignex);
\draw[cadre] (\gauche,\lignef) -- (\droite,\lignef);
\end{tikzpicture}
\end{center}
$$
</details>
