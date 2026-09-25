# Skew Hadamard difference sets from the Ree–Tits slice 2h+1 ✩ symplectic spreads in PG(3,3)

$$
3^{2h+1})^{ 宽 }
$$

## Cunsheng Ding <sup>a</sup>, Zeying Wang <sup>b</sup>, Qing Xiang <sup>b</sup>

a *Department of Computer Science, Hong Kong University of Science and Technology, Clear Water Bay,*
*Kowloon, Hong Kong*

b *Department of Mathematical Sciences, University of Delaware, Newark, DE 19716, USA*

#### Abstract

Received 7 February 2006

Available online 13 November 2006

$$
\mathrm{PG}(3,3^{2h+1})
$$

$$
\mathbb{F}_{3^{2h+1}}
$$

Using a class of permutation polynomials of F32h+1 obtained from the Ree–Tits slice symplectic spreads
h+1
in PG(3,32), we construct a family of skew Hadamard difference sets in the additive group of F32h+1.
With the help of a computer, we show that these skew Hadamard difference sets are new when *h* = 2 and
*h* = 3. We conjecture that they are always new when *h*>3. Furthermore, we present a variation of the
classical construction of the twin prime power difference sets, and show that inequivalent skew Hadamard
difference sets lead to inequivalent difference sets with twin prime power parameters.
© 2006 Elsevier Inc. All rights reserved.

$$
\mathbb{F}_{3^{2h+1}}
$$

$$
h=3
$$

*Keywords:* Difference set; Gauss sum; Permutation polynomial; Ree–Tits slice spread; Skew Hadamard difference set;
Symplectic spread; Twin prime power difference set

### 1. Introduction

Let *G* be a finite group of order *v* (written multiplicatively). A *k*-element subset *D* of *G* is
called a *(v, k, λ) difference set* if the list of “differences” *xy<sup>−1</sup>, x,y* ∈ *D, x*
= *y,* represents each
nonidentity element in *G* exactly *λ*<sub>q</sub>,times. As an example of difference sets, we mention the *+)* consisting of the nonzero squares of F<sub>q</sub>, where F<sub>q</sub>is
classical Paley difference set in the finite field of order *q,* and *q* (is a prime power congruent to 3 modulo 4. Difference sets are F
the subject of much study in the past 50 years. We assume that the reader is familiar with the

$$
xy^{-1},x,y\in D,x\ne y
$$

$$
\lambda
$$

$$
(\mathbb{F}_q,+)
$$

$$
q
$$

$$
\mathbb{F}_q
$$

$$
\mathbb{F}_q
$$

$$
q
$$

<sup>✩</sup>Research supported in part by NSF Grant DMS 0400411.

*E-mail addresses:* cding@ust.hk (C. Ding), wangz@math.udel.edu (Z. Wang), xiang@math.udel.edu (Q. Xiang).

0097-3165/$ – see front matter © 2006 Elsevier Inc. All rights reserved.
doi:10.1016/j.jcta.2006.09.008 basic theory of difference sets as can be found in [2,15], and [4, Chapter 6]. For a recent survey,
see [20].

A difference set *D* in a finite group *G* is called *skew Hadamard* if *G* is the disjoint union of
(−1) (−1) −1
*D, D,* and {1}, where *D* = {*d* | *d* ∈ D}. The aforementioned Paley difference set in
*(F*<sub>q</sub>*, +)* is an example of skew Hadamard difference sets. Let *D* be a *(v, k, λ)* skew Hadamard
difference set in an abelian group *G.* Then we have
v − 1 v − 3

$$
D,D^{(-1)}
$$

$$
D^{(-1)}=\{d^{-1}\mid d\in D\}
$$

$$
(\mathbb{F}_q,+)
$$

$$
1\notin D,\quad k=\frac{v-1}{2}\quad and\quad\lambda=\frac{v-3}{4}.
$$

If we employ group ring notation, then in Z[G], we have

$$
\begin{aligned}&DD^{(-1)}=\frac{v+1}{4}+\frac{v-3}{4}G,\\&D+D^{(-1)}=G-1,\\ \end{aligned}
$$

∑
(−1) −1
where *D* =d∈Dd. Applying any nonprincipal (complex) character *φ* of *G* to the above
two equations, one has
√

$$
D^{(-1)}=\sum_{d\in D}d^{-1}
$$

$$
\phi
$$

$$
\phi\left(D\right)=\frac{-1\pm\sqrt{-v}}{2}.
$$

(1.1)

Therefore the complex character values of a *(v, k, λ)* skew Hadamard abelian difference set all
√
lie in the quadratic extension *Q( −v)* of Q. This property of abelian skew Hadamard difference
sets places severe restrictions on these difference sets. Skew Hadamard difference sets were
studied by Johnsen [11], Camion and Mann [5], Jungnickel [12], and Chen, Xiang and Sehgal
[7]. The results in [5,7,11] can be summarized as follows:

$$
(v,k,\lambda)
$$

$$
\mathbb{Q}(\sqrt{-v})
$$

**Theorem 1.1.** *Let D be a (v, k, λ) skew Hadamard difference set in an abelian group G. Then v*
m
*is equal to a prime power p* ≡ 3 (mod *4), and the quadratic residues modulo v are multipliers*
s 3
*of D. Moreover, if G has exponent p with s 2, then s (m* + *1)/4. In particular, if v* = *p*
*or p<sup>5</sup>, then G must be elementary abelian.*

$$
p^{m}\equiv3
$$

$$
D.
$$

$$
p^{s}
$$

$$
s\geqslant2
$$

$$
v=p^{3}
$$

$$
s\leqslant(m+1)/4
$$

$$
p^{5}
$$

It was conjectured that if an abelian group *G* contains a skew Hadamard difference set, then
*G* has to be elementary abelian. This conjecture is still open in general. Theorem 1.1 contains all
known results on this conjecture. It was further conjectured some time ago that the Paley difference sets are the only examples of skew Hadamard difference sets in abelian groups. This latter
conjecture was recently disproved by Ding and Yuan [8], who constructed new skew Hadamard
difference sets in *(F*<sub>3</sub><sup>2</sup><sup>h</sup><sup>+1</sup>*, +)* by using certain planar functions related to Dickson polynomials.

$$
\left(\mathbb{F}_{3^{2h+1}},+\right)
$$

In this paper we construct new skew Hadamard difference sets by using certain permutation
polynomials [1] from the Ree–Tits slice symplectic spreads in PG(3,3<sup>2h+1</sup>). While the construction itself is quite simple (see Section 3), the proof that the candidate sets are indeed difference
sets is not so easy: we had to resort to a lemma in [7] and use Gauss sums and Stickelberger’s
theorem on the prime ideal factorization of Gauss sums. To make the paper self-contained, we
include a brief introduction to Gauss sums here.

$$
\mathrm{PG}(3,\dot{3}^{2h+1})
$$

m
Let *p* be a prime,q = *p.* Letξ
be the trace from F<sub>q</sub>to Z/pZ. Define

<sub>p</sub>be a fixed complex primitive pth root of unity and let Tr<sub>q/p</sub>

$$
q=p^{m}
$$

$$
\xi_{p}
$$

$$
\mathbb{F}_q
$$

$$
\mathrm{Tr}_{q/p}
$$

$$
\mathbb{Z}/p\mathbb{Z}
$$

$$
\psi:\mathbb{F}_{q}\to\mathbb{C}^{*},\qquad\psi(x)=\xi_{p}^{\mathrm{Tr}_{q/p}(x)},
$$

which is easily seen to be a nontrivial character of the additive group of F<sub>q</sub>. Let
∗ ∗

$$
\mathbb{F}_q
$$

$$
\chi:\mathbb{F}_q^*\to\mathbb{C}^*
$$

---

∗
be a character of F<sub>q</sub>(the cyclic multiplicative group of F
∑

<sub>q</sub>). We define the *Gauss sum* by

$$
\mathbb{F}_q^*
$$

$$
\mathbb{F}_q)
$$

$$
g(\chi)=\sum_{a\in\mathbb{F}_{q}^{*}}\chi(a)\psi(a).
$$

Note that if *χ*<sub>0</sub>is the trivial multiplicative character of F
viewed as the Fourier coefficients in the Fourier expansion of
∗
characters of F<sub>q</sub>. That is, for every *c* ∈ F<sub>q</sub>,
∑

<sub>q</sub>, then *g(χ*<sub>0</sub>*)* = −1. Gauss sums can be
*ψ*|<sub>F</sub>∗ in terms of the multiplicative
*q*

$$
\chi_{0}
$$

$$
\mathbb{F}_q
$$

$$
g(\chi_{0})=-1
$$

$$
\psi|\mathbb{F}_q^*
$$

$$
\mathbb{F}_q
$$

$$
c\in\mathbb{F}_q^*
$$

$$
\psi(c)=\frac{1}{q-1}\sum_{\chi\in X}g(\chi)\chi^{-1}(c),
$$

(1.2)

∗
where *X* denotes the character group of F<sub>q</sub>.

$$
\mathbb{F}_q^*
$$

One of the elementary properties of Gauss sums is [3, Theorem 1.1.4]

(1.3)

$$
g(\chi)\overline{{g(\chi)}}=q,\quad\mathrm{if}\chi\neq\chi_{0}.
$$

= *χ*
A deeper result on Gauss sums is Stickelberger’s theorem (Theorem 1.2 below) on the prime
ideal factorization of Gauss sums. We first introduce some notation. Let *a* be any integer not
divisible by *q* − 1. We use *L(a)* to denote the least positive integer congruent to *a* modulo *q* − 1.
Write *L(a)* to the base *p* so that

$$
q-1
$$

$$
L\left(a\right)
$$

$$
q-1
$$

$$
L(a)=a_{0}+a_{1}p+\cdots+a_{m-1}p^{m-1}
$$

where 0 *a*<sub>i</sub>*p* − 1 for all i,0 *i*

*m−* 1. We define the *digit sum* of *a* (mod *q* − 1) as

$$
0\leqslant a_{i}\leqslant p-1
$$

$$
i,0\leqslant i\leqslant m-1
$$

$$
q-1)
$$

$$
s(a)=a_{0}+a_{1}+\cdots+a_{m-1}.
$$

For integers *a* divisible by *q* − 1, we define

*s(a)* = 0.

$$
q-1
$$

$$
s(a)=0.
$$

Next let ξq−1be a complex primitive
lying over *p.* Then Z[ξq−1]/
the Teichmüller character on Fq
{

*(q* − 1)th root of unity. Fix any prime ideal p in Z[ξq−1]
p is a finite field of order *q,* which we identify with F<sub>q</sub>. Letω<sub>p</sub>be
, i.e., an isomorphism
}

$$
\xi_{q-1}
$$

$$
(q-1)
$$

$$
\mathbb{Z}[\xi_{q-1}]
$$

$$
p
$$

$$
\mathbb{Z}[\xi_{q-1}]/\mathfrak{p}
$$

$$
q
$$

$$
\mathbb{F}_q
$$

$$
\omega_{\mathfrak{p}}
$$

$$
\mathbb{F}_q,i.e.
$$

$$
\omega_{\mathfrak{p}}:\mathbb{F}_{q}^{*}\to\left\{1,\xi_{q-1},\xi_{q-1}^{2},\ldots,\xi_{q-1}^{q-2}\right\}
$$

satisfying

$$
\omega_{\mathfrak{p}}(\alpha)\pmod{\mathfrak{p}}=\alpha,
$$

(1.4)

∗
for all *α* in F<sub>q</sub>. The Teichmüller character
characters of F<sub>q</sub>.

*ω*<sub>p</sub>has order *q−* 1; hence it generates all multiplicative

$$
\mathbb{F}_q^*
$$

$$
\omega_{\mathfrak{p}}
$$

$$
q-1
$$

$$
\left[\mathbb{F}_q\right.
$$

−a
Let P be the prime ideal of Z[ξ<sub>q</sub><sup>−1</sup>*, ξ*<sub>p</sub>] lying above p. For an integer *a,* letν<sub>P</sub>*(g(ω*<sup>p</sup>*))*
−a
denote the P-adic valuation of *g(ω*<sub>p</sub>*).* The following classical theorem is due to Stickelberger
(see [16, p. 7], [3, p. 344]).

$$
\mathbb{Z}[\xi_{q-1},\xi_{p}]
$$

$$
\mathfrak{P}
$$

$$
v_{\mathfrak{P}}(g(\omega_{\mathfrak{p}}^{-a}))
$$

$$
a.
$$

$$
g(\omega_{\mathfrak{p}}^{-a})
$$

m
**Theorem 1.2.** *Let p be a prime, and q* = *p. Let a be any integer not divisible by q* − *1. Then*
( ())
−a
*νPg* ωp= *s(a).*

$$
q=p^{m}
$$

$$
q-1
$$

$$
v_{\mathfrak{P}}\left(g\left(\omega_{\mathfrak{p}}^{-a}\right)\right)=s(a).
$$

The paper is organized as follows. In Section 2, we give a brief introduction to symplectic
spreads in *PG(3,q),* and recall a theorem of Ball and Zieve [1] which shows that symplectic
spreads in *PG(3,q)* give rise to permutation polynomials of F<sub>q</sub>and vice versa. In particular,
we recall a class of permutation polynomials *f*<sub>a</sub>*(x)* of F<sub>3</sub>*m, a* ∈ F<sub>3</sub>*m,* coming from the Ree–
Tits slice symplectic spreads. In Section 3, we use the aforementioned permutation polynomials

$$
\mathbb{PG}(3,q)
$$

$$
\mathbb{F}_q
$$

$$
\mathbb{PG}(3,q)
$$

$$
f_{a}(x)
$$

$$
\mathbb{F}_{3^m},a\in\mathbb{F}_{3^m}
$$

---

*f*<sub>a</sub>*(x)* to construct skew Hadamard difference sets in *(F*<sub>3</sub>*m,* +). In Section 4, we address the
inequivalence issues for skew Hadamard difference sets in *(F*<sub>3</sub>*m,* +). Finally in Section 5, we
present a variation of the classical construction of the twin prime power difference sets. Also we
show that inequivalent skew Hadamard difference sets can give rise to inequivalent difference
sets with twin prime power parameters.

$$
\left(\mathbb{F}_{3^m},+\right)
$$

$$
f_{a}(x)
$$

$$
\left(\mathbb{F}_{3^m},+\right)
$$

### 2. A class of permutation polynomials from the Ree–Tits slice symplectic spreads in 2h<sup>+1</sup> PG(3,3<em>)</em>

$$
\mathbf{PG}(3,3^{2h+1})
$$

4
Let *PG(3,q)* denote the 3-dimensional projective space over F<sub>q</sub>, and let *V* = F<sub>q</sub>be the underlying vector space of *PG(3,q).Aspread* of PG(3,q)is a partition of the points of the space
into lines. Now we equip *V* with a nondegenerate alternating form *B* : *V* × *V* → F<sub>q</sub>. A spread
of PG(3,q)is called *symplectic* if every line of the spread is totally isotropic with respect to *B.*
Since all nondegenerate alternating forms on *V* are equivalent, we may assume that *B* is defined
as follows:
()

$$
\mathbb{PG}(3,q)
$$

$$
\mathbb{F}_q
$$

$$
V=\mathbb{F}_q^4
$$

$$
\mathbb{PG}(3,q)
$$

$$
\mathrm{PG}(3,q)
$$

$$
B\colon V\times V\to\mathbb{F}_q.A
$$

$$
\mathbb{PG}(3,q)
$$

$$
B\left(\left(x_{0},x_{1},x_{2},x_{3}\right),\left(y_{0},y_{1},y_{2},y_{3}\right)\right)=x_{0}y_{3}-x_{3}y_{0}-x_{1}y_{2}+y_{1}x_{2}.
$$

(2.1)

Then a symplectic spread is a partition of the points of PG(3,q)into lines such that *B(P,Q)* = 0
for any points *P, Q* lying on the same line of the spread. For readers who are familiar with
classical generalized quadrangles, a symplectic spread of *PG(3,q)* is nothing but a spread of
the classical generalized quadrangle *W*<sub>3</sub>*(q).* By the Klein correspondence (see [9]), a spread of
*W*<sub>3</sub>*(q)* corresponds to an ovoid of the classical generalized quadrangle *Q(4,q).*

$$
\mathbb{PG}(3,q)
$$

$$
B(P,Q)=0
$$

$$
P,\ Q
$$

$$
\mathrm{PG}(3,q)
$$

$$
W_{3}(q)
$$

$$
W_{3}(q)
$$

$$
Q(4,q)
$$

In [1], it was shown that every symplectic spread of *PG(3,q)* gives rise to a certain family
of permutation polynomials of F<sub>q</sub>and vice versa. Since the symplectic group *Sp(V )* leaving the
alternating form in (2.1) invariant acts transitively on the set of totally isotropic lines, we may
assume that the symplectic spread under consideration contains the line
〈 〉

$$
\mathbb{PG}(3,q)
$$

$$
\mathbb{F}_q
$$

$$
\mathrm{Sp}(V)
$$

$$
\ell_{\infty}=\left\langle(0,0,0,1),(0,0,1,0)\right\rangle.
$$

**Theorem 2.1.** [1] *The set of totally isotropic lines*
{〈 ()〉 ∣

$$
\ell_{\infty}\cup\left\{\left\langle(0,1,x,y),(1,0,-y,g(x,y))\right\rangle\mid x,y\in\mathbb{F}_{q}\right\}
$$

*is a symplectic spread of PG(3,q) if and only if*

(2.2)

$$
x\mapsto g(x,ax-b)+a^{2}x
$$

→ *g(x,ax −b)+ a*
*is a permutation of* F<sub>q</sub>*for all a, b* ∈ F<sub>q</sub>*.*

$$
\mathbb{F}_q
$$

$$
b\in\mathbb{F}_q.
$$

Table 1 in [1] lists all known symplectic spreads of *PG(3,q).* For our purpose of constructing
new skew Hadamard difference sets, we are interested in the Ree–Tits slice symplectic spread,
which is a spread having the form (2.2), with

$$
\mathbb{PG}(3,q)
$$

$$
g(x,y)=-x^{2\alpha+3}-y^{\alpha}
$$

√
2h+1
where *q* = 3 and *α* = 3q. This spread was discovered by Kantor [14] as an ovoid of
*Q(4,q),* which is a slice of the Ree–Tits ovoid of *Q(6,q).*

$$
q=3^{2h+1}
$$

$$
\alpha=\sqrt{3q}
$$

$$
Q(4,q)
$$

$$
Q(6,q)
$$

By Theorem 2.1 the Ree–Tits example gives us a class of permutation polynomials, namely,
α 2
the polynomials *f*<sub>a</sub>*(x)* = *b −(g(x, ax −b)+ a x), a* ∈ F<sub>q</sub>. Explicitly, we have

$$
f_{a}(x)=b^{\alpha}-(g(x,ax-b)+a^{2}x),a\in\mathbb{F}_{q}
$$

$$
f_{a}(x)=x^{2\alpha+3}+(ax)^{\alpha}-a^{2}x.
$$

(2.3)

---

As commented in [1], the polynomial *f*<sup>a</sup>is remarkable in that it is a permutation polynomial of
√
F<sub>q</sub>whose degree is approximately *q.* There are only a handful of known permutation polynomials with such a low degree. A direct proof that *f*<sub>a</sub>*(x)* is a permutation polynomial can be found
in [1].

$$
f_{a}
$$

$$
\sqrt{q}
$$

$$
\mathbb{F}_q
$$

$$
f_{a}(x)
$$

We comment that by going through Table 1 in [1], one can see that all other permutation polynomials arising from known symplectic spreads of *PG(3,q), q* odd, are linearized permutation
polynomials of F<sub>q</sub>, which will not lead to new skew Hadamard difference sets by the construction described below. That is the reason why we only choose to work with the polynomials *f*<sub>a</sub>*(x)*
defined in (2.3).

$$
\mathbb{PG}(3,q)
$$

$$
\mathbb{F}_q
$$

$$
f_{a}(x)
$$

### 3. A construction of skew Hadamard difference sets

m
Throughout this section, *q* = 3, where *m* = *2h* + 1, *h* 0. For any *a* ∈ F<sub>q</sub>, letf<sub>a</sub>*(x)* be the
polynomial defined in (2.3). As seen in Section 2, *f*<sub>a</sub>*(x)* is a permutation polynomial of F<sub>q</sub>. For
any nonzero *a* ∈ F<sub>q</sub>, let
{ () ∣}

$$
q=3^{m}
$$

$$
m=2h+1,h\geqslant0
$$

$$
a\in\mathbb{F}_q
$$

$$
f_{a}(x)
$$

$$
f_{a}(x)
$$

$$
\mathbb{F}_q
$$

$$
a\in\mathbb{F}_q
$$

$$
D_{a}=\left\{f_{a}\left(x^{2}\right)\mid x\in\mathbb{F}_{q}^{*}\right\},
$$

(3.1)

∗
where F<sub>q</sub>= F<sub>q</sub>\ {0}. We will show that *D*<sub>a</sub>is a skew Hadamard difference set in *(F*<sub>q</sub>*,* +). We
start with the following

$$
\mathbb{F}_q^*=\mathbb{F}_q\setminus\{0\}
$$

$$
D_{a}
$$

$$
(\mathbb{F}_q,+)
$$

**Lemma 3.1.** *For any nonzero a* ∈ F<sub>q</sub>*, we have*

$$
a\in\mathbb{F}_q
$$

$$
D_{a}\cap(-D_{a})=\varnothing,
$$

*and*

$$
D_{a}\cup(-D_{a})\cup\{0\}=\mathbb{F}_{q}.
$$

2 2 ∗
**Proof.** Assume that *f*<sub>a</sub>*(x)* = *−f*<sub>a</sub>*(y)* for some *x,y* ∈ F<sub>q</sub>. Then
() ()

$$
f_{a}(x^{2})=-f_{a}(y^{2})
$$

$$
x,y\in\mathbb{F}_q^*
$$

$$
f_{a}(x^{2})=f_{a}(-y^{2}).
$$

Since *f*<sub>a</sub>*(x)* is a permutation polynomial of F
square in F<sub>q</sub>. But−1 is not a square in F<sub>q</sub>
contradiction. Hence *D*<sub>a</sub>∩ *(−D*<sub>a</sub>*)* = ∅.

2 2
<sub>q</sub>, we havex = −y, which implies that −1 isa
m
, since *q* = 3 and *m* is odd. Therefore we reached a

$$
f_{a}(x)
$$

$$
\mathbb{F}_q
$$

$$
x^{2}=-y^{2}
$$

$$
\mathbb{F}_q.\mathrm{But}-1
$$

$$
\mathbb{F}_q
$$

$$
q=3^{m}
$$

$$
D_{a}\cap(-D_{a})=\varnothing
$$

Next, clearly we have *f*<sup>a</sup>*(0)* = 0. Since *f*<sup>a</sup>*(x)* is a permutation polynomial of F<sub>q</sub>, we see that
2
*f*<sub>a</sub>*(x)* = 0 if and only if *x* = 0. Therefore 0 *∈/ D*<sub>a</sub>. The second assertion of the lemma now
follows easily. This completes the proof. ✷

$$
f_{a}(0)=0
$$

$$
f_{a}(x)
$$

$$
f_{a}(x^{2})=0
$$

$$
\mathbb{F}_q
$$

$$
x=0
$$

$$
0\notin D_{a}
$$

We will use the character sum approach (see, e.g., [4, p. 318]) to prove that *D*<sub>a</sub>is a difference
set. Using this approach, in order to show that *D*<sub>a</sub>is a difference set, we must prove that for any
nontrivial additive character *ψ* of F<sub>q</sub>,

$$
D_{a}
$$

$$
D_{a}
$$

$$
\psi
$$

$$
\mathbb{F}_q
$$

$$
\psi\left(D_{a}\right)\overline{{\psi\left(D_{a}\right)}}=\frac{q+1}{4}.
$$

(3.2)

It seems difficult to prove directly that (3.2) holds for every nontrivial additive characters *ψ*
of F<sub>q</sub>. We will use a lemma in [7] to bypass this difficulty.

$$
\psi
$$

$$
\mathbb{F}_q
$$

---

**Lemma 3.2.** [7] *Let G be a (multiplicative) abelian p-group of order p<sup>m</sup>, where p is a prime
congruent to* 3 *modulo 4, and m is an odd integer. Let D be a subset of G such that in* Z[G],

$$
p^{m}
$$

$$
D+D^{(-1)}=G-1,
$$

*and D<sup>(t)</sup>* = *D for every nonzero quadratic residue t modulo p. If for every nontrivial character
φ of G,*

$$
D^{(t)}=D
$$

$$
\phi
$$

$$
\phi\left(D\right)\equiv\frac{p^{\left(m-1\right)/2}-1}{2}\pmod{p^{\left(m-1\right)/2}},
$$

*then D is a difference set in G.*

The idea of Lemma 3.2 is that sometimes congruence properties of *φ(D)can* be used to determine the (complex) absolute value of *φ(D).* The proof of the lemma relies on Fourier inversions,
and can be found in [7].

$$
\phi(D)
$$

$$
\phi\left(D\right)
$$

We now state the main theorem of this section.

∗
**Theorem 3.3.** *Let a* ∈ F<sub>q</sub>*, and let D*<sub>a</sub>*be defined as in* (3.1). *Then D*<sub>a</sub>*is a skew Hadamard
difference set in (F*<sub>q</sub>*, +).*

$$
a\in\mathbb{F}_q^*
$$

$$
D_{a}
$$

$$
D_{a}
$$

$$
(\mathbb{F}_q,+)
$$

**Proof.** By Lemma 3.1, we know that *D*<sub>a</sub>is skew. Since 1 ∈ Z/3Z is the only nonzero quadratic
residue modulo 3, we certainly have *D*<sub>a(t)</sub>= *D*<sub>a</sub>for every nonzero quadratic residue *t* modulo 3.
Therefore by Lemma 3.2, it suffices to show that for every nontrivial additive character *ψ*<sub>β</sub>:
∗
F<sub>q</sub>→ C,

$$
D_{a}
$$

$$
1\in\mathbb{Z}/3\mathbb{Z}
$$

$$
D_{a}^{(t)}=D_{a}
$$

$$
\psi_{\beta}
$$

$$
\mathbb{F}_q\to\mathbb{C}^*
$$

$$
\psi_{\beta}(D_{a})\equiv\frac{3^{(m-1)/2}-1}{2}\pmod{3^{(m-1)/2}},
$$

(3.3)

Tr(βx)
where *ψ*<sup>β</sup>*(x)* = *ξ, ξ*<sup>3</sup>
3

2πi/3
= *e,* and Tr is the absolute trace from F<sub>q</sub>to F<sub>3</sub>.

$$
\psi_{\beta}(x)=\xi_{3}^{\mathrm{Tr}(\beta x)},\xi_{3}=e^{2\pi i/3}
$$

$$
\mathbb{F}_q
$$

$$
\mathbb{F}_{3}
$$

We now compute *ψ*<sub>β</sub>*(D*

*a).* Letχ be the (multiplicative) quadratic character of Fq. Then
( ∑

$$
\psi_{\beta}(D_{a})
$$

$$
\chi
$$

$$
\mathbb{F}_q
$$

$$
\begin{align*}\psi_{\beta}(D_a)&=\sum_{x\in\mathbb{F}_q^*}\psi_{\beta}\big(f_a(x)\big)\frac{(\chi(x)+1)}{2}=\frac{1}{2}\Bigg(\sum_{x\in\mathbb{F}_q^*}\psi_{\beta}\big(f_a(x)\big)\chi(x)+\sum_{x\in\mathbb{F}_q^*}\psi_{\beta}\big(f_a(x)\big)\Bigg)\\&=\frac{1}{2}\Bigg(\sum_{x\in\mathbb{F}_q^*}\psi_{\beta}\big(f_a(x)\big)\chi(x)-1\Bigg),\end{align*}
$$

where in the last equality we used the facts that *f*<sub>a</sub>*(x)* is a permutation polynomial of F<sub>q</sub>and
*f*<sub>a</sub>*(0)* = 0. From this last expression for *ψ*<sub>β</sub>*(D*<sub>a</sub>*),* we see that (3.3) is equivalent to
∑ () ()

$$
f_{a}(x)
$$

$$
f_{a}(0)=0
$$

$$
\mathbb{F}_q
$$

$$
\psi_{\beta}(D_{a})
$$

$$
\sum_{x\in\mathbb{F}_{q}^{*}}\psi_{\beta}\left(f_{a}(x)\right)\chi(x)\equiv0\pmod{3^{h}}.
$$

(3.4)

∑
Let Sβ=x∈F∗ ψβ(fa
*q*

*(x))χ(x).* Wehave

$$
S_{\beta}=\sum_{x\in\mathbb{F}_{q}^{*}}\psi_{\beta}(f_{a}(x))\chi(x).\mathbb{V}
$$

$$
\begin{align*}S_{\beta}=&\sum_{x\in\mathbb{F}_q^*}\xi_3^{\mathrm{Tr}(\beta x^{2\alpha+3}+(\beta a^\alpha-\beta^\alpha a^{2\alpha})x^\alpha)}\chi(x)=\sum_{y\in\mathbb{F}_q^*}\xi_3^{\mathrm{Tr}(\beta y^{\alpha+2}+(\beta a^\alpha-\beta^\alpha a^{2\alpha})y)}\chi(y)\\=&\pm\sum_{y\in\mathbb{F}_q^*}\xi_3^{\mathrm{Tr}(y^{\alpha+2}+(\beta^{\alpha-1}a^\alpha-\beta^{2\alpha-2}a^{2\alpha})y)}\chi(y).\end{align*}
$$

---

α−1 α 2α
Let *γ*<sub>a</sub>= *β a* − *β*
evaluated exactly (see [17, p. 199]). Indeed, if
∑

−2 2α
*a.* Ifγ<sub>a</sub>= 0, then
*γ*
∑

S<sub>β</sub>is a quadratic Gauss sum, which can be
<sub>a</sub>= 0, then we have
√

$$
\gamma_{a}=\beta^{\alpha-1}a^{\alpha}-\beta^{2\alpha-2}a^{2\alpha}
$$

$$
\gamma_{a}=0
$$

$$
S_{\beta}
$$

$$
\gamma_{a}=0
$$

$$
\begin{align*}S_{\beta}=&\pm\sum_{y\in\mathbb{F}_q^*}\xi_3^{\mathrm{Tr}(y^{\alpha+2})}\chi(y)=\pm\sum_{z\in\mathbb{F}_q^*}\xi_3^{\mathrm{Tr}(z)}\chi(z)=\pm g(\chi)=\pm\sqrt{-q}\\=&\pm3^h\sqrt{-3}\equiv0\pmod{3^h}.\end{align*}
$$

Hence in this case, *(3.4)* is true. To finish the proof, it suffices to prove that when *γ*<sub>a</sub>
() = 0,

$$
\gamma_{a}\neq0
$$

$$
\sum_{y\in\mathbb{F}_q^*}\xi_3^{\mathrm{Tr}(y^{\alpha+2}+\gamma_a y)}\chi(y)\equiv0\pmod{3^h}.
$$

(3.5)

Now using Fourier inversion (e.g., see (1.2)), we have for any

∗
*y* ∈ F<sub>q</sub>,

$$
y\in\mathbb{F}_q^*
$$

$$
\xi_{3}^{\mathrm{Tr}(y)}=\frac{1}{q-1}\sum_{b=0}^{q-2}g\left(\omega^{-b}\right)\omega^{b}(y),
$$

where *ω* is the Teichmüller character on F
∑

<sub>q</sub>. Then

$$
\mathbb{F}_q
$$

$$
\begin{align*}&\sum_{y\in\mathbb{F}_q^*}\xi_3^{\mathrm{Tr}(y^{\alpha+2}+\gamma_a y)}\chi\left(y\right)\\&\quad=\sum_{y\in\mathbb{F}_q^*}\xi_3^{\mathrm{Tr}(\gamma_a y)}\chi\left(y\right)\cdot\frac{1}{q-1}\sum_{b=0}^{q-2}g\big(\omega^{-b}\big)\omega^b\big(y^{\alpha+2}\big)\\&\quad=\sum_{y\in\mathbb{F}_q^*}\xi_3^{\mathrm{Tr}(\gamma_a y)}\omega^{-\frac{q-1}{2}}\big(y\big)\cdot\frac{1}{q-1}\sum_{b=0}^{q-2}g\big(\omega^{-b}\big)\omega^{b(\alpha+2)}\big(y\big)\\&\quad=\frac{1}{q-1}\sum_{b=0}^{q-2}g\big(\omega^{-b}\big)\sum_{y\in\mathbb{F}_q^*}\xi_3^{\mathrm{Tr}(\gamma_a y)}\omega^{-\frac{q-1}{2}+b(\alpha+2)}\big(y\big)\\&\quad=\frac{1}{q-1}\sum_{b=0}^{q-2}g\big(\omega^{-b}\big)g\big(\omega^{-\frac{q-1}{2}+b(\alpha+2)}\big)\omega^{-\frac{q-1}{2}+b(\alpha+2)}\big(\gamma_a^{-1}\big).\end{align*}
$$

Hence, we have

$$
S_{\beta}=\pm\frac{1}{q-1}\sum_{b=0}^{q-2}g\left(\omega^{-b}\right)g\left(\omega^{-\frac{q-1}{2}+b(\alpha+2)}\right)\omega^{-\frac{q-1}{2}+b(\alpha+2)}\left(\gamma_{a}^{-1}\right).
$$

(3.6)

Fix any prime ideal p in Z[
above p. Since *ν*<sub>P</sub>*(3)*
()

*ξ*<sub>q</sub>−1] lying over 3. Let P be the prime ideal of Z[ξ<sub>q</sub>−1, *ξ*<sub>3</sub>] lying
= 2, we see that

$$
\mathbb{Z}[\xi_{q-1}]
$$

$$
\mathfrak{P}
$$

$$
\mathbb{Z}[\xi_{q-1}
$$

$$
v_{\mathfrak{P}}(3)=2
$$

$$
S_{\beta}\equiv0\pmod{3^{h}}\quad\Leftrightarrow\quad v_{\mathfrak{P}}(S_{\beta})\geqslant2h.
$$

Using the expression in (3.6) for

*S*<sub>β</sub>, we have
(

$$
S_{\beta}
$$

$$
S_{\beta}\equiv0\pmod{3^{h}}\quad\Leftrightarrow\quad v_{\mathfrak{P}}\left(\sum_{b=0}^{q-2}g\left(\omega^{-b}\right)g\left(\omega^{-\frac{q-1}{2}+b(\alpha+2)}\right)\omega^{-\frac{q-1}{2}+b(\alpha+2)}\left(\gamma_{a}^{-1}\right)\right)\geqslant2h.
$$

(3.7)

---

By Theorem 1.2 and the fact that
of F<sub>q</sub>, we have for any b,0 *b*

*g(χ*<sub>0</sub>*)
q* − 2,

= −1, where *χ*<sub>0</sub>is the trivial multiplicative character
()

$$
g(\chi_{0})=-1
$$

$$
\chi_{0}
$$

$$
\mathbb{F}_q
$$

$$
b,0\leqslant b\leqslant q-2
$$

$$
\nu\varphi\left(g\left(\omega^{-b}\right)g\left(\omega^{-\frac{q-1}{2}+b(\alpha+2)}\right)\right)=s(b)+s\left(\frac{q-1}{2}-b(\alpha+2)\right).
$$

Therefore if we can prove that for each
(

b,0 *b*
)

*q* − 2,

$$
b,0\leqslant b\leqslant q-2,
$$

$$
s\left(b\right)+s\left(\frac{q-1}{2}-b\left(\alpha+2\right)\right)\geqslant2h,
$$

(3.8)

then (3.5) will follow. This is exactly what we will do. In fact, we prove a slightly stronger inequality in Theorem A.1. (Since the proof of Theorem A.1 is somewhat lengthy, we put it in
Appendix A.) Now combine Theorem A.1 and Lemma 3.2, the proof of the theorem is complete. ✷

It is of interest to record the following corollary of Theorem 3.3.

m h+1 ∗ ∗
**Corollary 3.4.** *Let q* = *3, m* = 2h+ *1, and α* = *3. For any β* ∈ F<sub>q</sub>*and a* ∈ F<sub>q</sub>*, we have*
∑ √

$$
q=3^{m},m=2h+1
$$

$$
\alpha=3^{h+1}
$$

$$
\beta\in\mathbb{F}_q^*
$$

$$
a\in\mathbb{F}_q^*
$$

$$
\sum_{x\in\mathbb{F}_q^*}\chi(x)\xi_3^{\mathrm{Tr}(x^{\alpha+2}+(\beta^{\alpha-1}a^{\alpha}-\beta^{2(\alpha-1)}a^{2\alpha})x)}=\pm\sqrt{-q}.
$$

### 4. Inequivalence of skew Hadamard difference sets

Let *D*<sub>1</sub>and *D*<sub>2</sub>be two *(v, k,* λ)difference sets in an abelian group *G.* We say that *D*<sub>1</sub>and *D*<sub>2</sub>
are *equivalent* if there exists an automorphism *σ* of *G* and an element *g* ∈ *G* such that *σ(D*<sub>1</sub>*)* =
*D*<sub>2</sub>*g.* In this section, we discuss the inequivalence issues for skew Hadamard difference sets.

$$
D_{1}
$$

$$
D_{2}
$$

$$
(v,k,\lambda)
$$

$$
D_{2}
$$

$$
D_{1}
$$

$$
g\in G
$$

$$
\sigma(D_{l})=
D_{2}g
$$

#### 4.1. The known families of skew Hadamard difference sets

Let *a* ∈ F<sub>q</sub>and let *n* be a positive integer. We define the *Dickson polynomial D*<sub>n</sub>*(x, a)* over
F<sub>q</sub>by
()

$$
a\in\mathbb{F}_q
$$

$$
\mathcal{D}_{n}(x,a)
$$

$$
\mathbb{F}_q
$$

$$
\mathcal{D}_{n}(x,a)=\sum_{j=0}^{\lfloor n/2\rfloor}\frac{n}{n-j}\binom{n-j}{j}(-a)^{j}x^{n-2j},
$$

where *n/2* is the largest integer *n/2.* It is well known that the Dickson polynomial *D*<sup>n</sup>*(x, a),*
∗ 2
*a* ∈ F<sub>q</sub>, is a permutation polynomial of F<sub>q</sub>if and only if *gcd(n, q* − *1)* = 1 (see [17, p. 356]).
∗
Let m be a positive odd integer. For any u ∈ F <sub>m</sub>, define
3
()

$$
\left\lfloor n/2\right\rfloor
$$

$$
\leqslant n/2
$$

$$
\mathcal{D}_{n}(x,a)
$$

$$
a\in\mathbb{F}_q^*,
$$

$$
\mathbb{F}_q
$$

$$
\mathrm{gcd}(n,q^2-1)=1
$$

$$
u\in\mathbb{F}_{3^m}^*
$$

$$
g_{u}(x)=\mathcal{D}_{5}(x^{2},-u)=x^{10}-u x^{6}-u^{2}x^{2}.
$$

It was proved in [8] that when *m* is a positive odd integer and
Hadamard difference set in *(F*<sub>3</sub>*m, +)*
{ ∣}
∣

∗
u ∈ F <sub>m</sub>, Image(gu)\ {0} is a skew
3
. For convenience, we set

$$
u\in\mathbb{F}_{3^m}^*
$$

$$
\mathrm{Image}(g_u)\setminus\{0\}
$$

$$
\left(\mathbb{F}_{3^m},+\right)
$$

$$
\mathrm{DY}(u)=\left\{x^{10}-u x^{6}-u^{2}x^{2}\mid x\in\mathbb{F}_{3^{m}}^{*}\right\},
$$

and call these *the Ding–Yuan difference sets*

. We have *the* following proposition.

**Proposition 4.1.** *All previously known skew Hadamard difference sets are equivalent to one of
the following:*

---

$$
\mathbb{F}_q,
$$

$$
q\equiv3
$$

(1) *The Paley difference set P in* F

<sub>q</sub>*, where q* ≡ 3 (mod *4) is a prime power.*

(2) *The Ding–Yuan difference set*

DY(1) *in* F<sub>3</sub>*m*

*, where m is odd.*

$$
\mathbb{F}_{3^{m}}
$$

(3) *The Ding–Yuan difference set*

DY(−1) *in* F<sub>3</sub>*m*

*, where m is odd.*

$$
\mathbb{F}_{3^{m}}
$$

**Proof.** First of all, it can be checked directly that
()

*D*<sub>5</sub>*(−x,u)= −D*<sub>5</sub>*(x, u)* and

$$
\mathcal{D}_{5}(-x,u)=-\mathcal{D}_{5}(x,u)
$$

$$
b^{5}\mathcal{D}_{5}(x,a)=\mathcal{D}_{5}(b x,b^{2}a),\quad\forall a,b\in\mathbb{F}_{q}.
$$

(4.1)

Setting *a* = −1 in (4.1), we have
() (

$$
b^{5}\mathcal{D}_{5}(x^{2},-1)=\mathcal{D}_{5}(bx^{2},-b^{2}).
$$

2 5
Thus, we have *DY(b)* = *b* DY(1) if *b*
*b* is a nonsquare. Hence for any nonzero square *u*

m2 5
is a nonzero square in F<sub>3</sub>; and *DY(b)* = *−b* DY(1) if
∈ F<sub>3</sub>*m, DY(u)* is equivalent to DY(1).

$$
\mathrm{DY}(b^2)=b^5\mathrm{DY}(1)
$$

$$
\mathbb{F}_{3^{m}}
$$

$$
\mathrm{DY}(b^{2})=-b^{5}\mathrm{DY}(1)
$$

$$
u\in\mathbb{F}_{3^m}
$$

Similarly, we can prove that for any nonsquare

*u* ∈ F<sub>3</sub>*m, DY(u)* is equivalent to DY(−1).

$$
u\in\mathbb{F}_{3^m},\mathrm{DY}(u)
$$

Combining the above observation with the fact that the Paley family and the Ding–Yuan family were the only previously known skew Hadamard difference sets, we see that the proof of the
proposition is complete. ✷

With the help of a computer, it was verified in [8] that the three skew Hadamard difference
sets *P,* DY(1) and DY(−1) in *(F*<sub>3</sub>*m, +)* are all equivalent when *m* = 3, but they are indeed
pairwise inequivalent when *m* = 5 and 7. It is very likely that the three difference sets *P,* DY(1)
and DY(−1) are pairwise inequivalent for all odd *m*>7, although this is not proved rigorously.

$$
\left(\mathbb{F}_{3^m},+\right)
$$

$$
m=5
$$

*4.2. The inequivalence issues for the difference sets D*<sub>a</sub>

$$
D_{a}
$$

We now turn to the difference sets *D*<sub>a</sub>constructed in Section 3. First we prove the following

$$
D_{a}
$$

∗
Proposition 4.2. Let m = 2h + 1 be a positive integer and let a ∈ F <sub>m</sub>. The skew Hadamard
3
*difference sets D*<sub>a</sub>*in (F*<sub>3</sub>*m, +) constructed in Section* 3 *are equivalent to one of the following:*

$$
m=2h+1
$$

$$
a\in\mathbb{F}_{3^m}^*
$$

$$
D_{a}
$$

$$
(\mathbb{F}_{3^m},+)
$$

(1) *The difference set D*<sub>1</sub>*in (F*<sub>3</sub>*m, +).*

$$
D_{1}\;in\;(\mathbb{F}_{3^{m}},+).
$$

(2) *The difference set D*<sub>−1</sub>*in (F*<sub>3</sub>*m, +).*

$$
D_{-1}\;in\;(\mathbb{F}_{3^m},+).
$$

**Proof.** Using the definition of *f*<sub>a</sub>*(x)* in (2.3), it can be checked that
()

$$
f_{a}(x)
$$

$$
b^{2\alpha+3}f_{a}\left(\frac{x}{b}\right)=f_{a b^{\alpha+1}}(x),\quad\forall b\in\mathbb{F}_{3^{m}}^{*}.
$$

Assume that *a* is a nonzero square in F
such that

*m∗*
3. Since gcd(α + *1,q− 1)* = 2, one can find *ζ* ∈ *Fm*
3

$$
\mathbb{F}_{3^{m}}
$$

$$
\zeta\in\mathbb{F}_{3^m}^*
$$

$$
a\zeta^{\alpha+1}=1.
$$

$$
\zeta^{2\alpha+3}f_{a}\left(\frac{x^{2}}{\zeta}\right)=f_{1}\left(x^{2}\right).
$$

Hence

(4.2)

We note that if *ζ* is a square, then {
x2
a nonsquare, then {*f*<sub>a</sub>*()* | *x* ∈ F
ζ
Therefore

x2
∗ 2
fa() | x ∈ F <sub>m</sub>} = {fa(x) | x
ζ 3
∗ 2 ∗
<sub>m</sub>} = {fa(−x) | x ∈ F <sub>m</sub>} = {−f
3 3

∗
∈ F <sub>m</sub>}=Da; and if ζ is
3
2 ∗
*a(x*) | *x* ∈ Fq} = *−Da.*

$$
\zeta
$$

$$
\{f_{\alpha}(\frac{x^{2}}{\xi})\mid x\in\mathbb{F}_{3^{m}}^{*}\}=\{f_{\alpha}(x^{2})\mid x\in\mathbb{F}_{3^{m}}^{*}\}=D_{\alpha}
$$

$$
\{f_{a}(\frac{x^{2}}{\zeta})\mid x\in\mathbb{F}_{3^{m}}^{*}\}=\{f_{a}(-x^{2})\mid x\in\mathbb{F}_{3^{m}}^{*}\}=\{-f_{a}(x^{2})\mid x\in\mathbb{F}_{q}^{*}\}=-D_{a},
$$

---

$$
\left\{\zeta^{2\alpha+3}f_{a}\left(\frac{x^{2}}{\zeta}\right)\biggm|x\in\mathbb{F}_{3^{m}}^{*}\right\}=\zeta^{2\alpha+3}D_{a}\quad\mathrm{or}\quad-\zeta^{2\alpha+3}D_{a}.
$$

(4.3)

Combining (4.3) with (4.2), we see that *D*

<sub>a</sub>is equivalent to *D*<sub>1</sub>.

$$
D_{a}
$$

$$
D_{1}
$$

Similarly, we can show that *D*<sub>a</sub>is equivalent to *D*<sub>−1</sub>when *a* is a nonsquare in F<sub>3</sub>*m.* ✷

$$
D_{-1}
$$

$$
D_{a}
$$

$$
\mathbb{F}_{3^{m}}
$$

Since equivalent difference sets give rise to isomorphic symmetric designs, which have the
same *p*-rank and Smith normal form, we may use *p*-ranks and Smith normal forms to distinguish
inequivalent difference sets. See [20] for a recent survey of results on this subject. Unfortunately,
skew Hadamard difference sets with the same parameters have the samep-rank [13, pp. 297–299]
and the same Smith normal form [18]. Thus in order to distinguish inequivalent skew Hadamard
difference sets, we have to use some other techniques.

It seems not easy to settle completely the question whether the difference sets *D*<sub>1</sub>and *D*<sub>−1</sub>
are inequivalent to the previously known families stated in Proposition 4.1. With the aid of a
computer, we will show that the skew Hadamard difference sets *D*<sub>1</sub>and *D*<sub>−1</sub>in *(F*<sub>3</sub>*m, +)* are
new when *m* = 5 and 7. (We mention that when *m* = 3, the difference sets *D*<sub>1</sub>and *D*<sub>−1</sub>are
equivalent to the Paley difference set in F<sub>3</sub><sup>3</sup>.)

$$
D_{1}
$$

$$
D_{-1}
$$

$$
D_{1}
$$

$$
D_{-1}
$$

$$
\left(\mathbb{F}_{3^m},+\right)
$$

$$
m=5
$$

$$
m=3
$$

$$
D_{-1}
$$

$$
D_{1}
$$

$$
\mathbb{F}_{3^{3}}.)
$$

Let *D* be a difference set in *(F*<sub>q</sub>*, +)*
∣

∗
. For any 2-subset {a,b}⊂F<sub>q</sub>, we define
∣

$$
(\mathbb{F}_q,+)
$$

$$
\left\{a,b\right\}\subset\mathbb{F}_{q}^{*}
$$

$$
T\{a,b\}:=\left|D\cap(D+a)\cap(D+b)\right|.
$$

These numbers *T {a,b}* are called the *triple intersection numbers,* which were used to distinguish
inequivalent difference sets in 1971 by Baumert [2, p. 144].

$$
T\{a,b\}
$$

We shall use the triple intersection numbers to distinguish the skew difference sets of this
paper from the earlier ones in the cases where *m* = 5 and *m* = 7. We use *P* and *RT(a)* to denote
the Paley difference set and the difference set *D*<sub>a</sub>from Section 3, respectively.

$$
m=5
$$

$$
m=7
$$

$$
D_{a}
$$

With the help of Magma [6], the maximum and minimum triple intersection numbers of these
difference sets in F37 are computed and listed below.

$$
\mathbb{F}_{3^{7}}
$$

| Difference set | Minimum (when m = 7) | Maximum (when m = 7) |
| --- | --- | --- |
| P | 261 | 284 |
| DY(1) | 246 | 300 |
| DY(-1) | 248 | 297 |
| RT(1) | 250 | 295 |
| RT(-1) | 249 | 296 |

$$
m=7)
$$

Hence the five difference sets are pairwise inequivalent when *m* = 7. It then follows from Proposition 4.1 that the skew difference sets RT(1) and RT(−1) are new when *m* = 7.

When *m* = 5, the maximum and minimum triple intersection numbers of these difference sets
in F<sub>3</sub>*m* are computed and listed below.

| Difference set | Minimum (when m = 5) | Maximum (when m = 5) |
| --- | --- | --- |
| P | 26 | 33 |
| DY(1) | 23 | 36 |
| DY(-1) | 24 | 35 |
| RT(1) | 24 | 35 |
| RT(-1) | 24 | 35 |

---

In fact, in this case DY(−1), RT(1) and RT(−1) have the same set of triple intersection numbers,
i.e., {i: 24 *i* 35}. We further compute the multiplicities of these triple intersection numbers
for these three cases. We find the following data.

$$
24\leqslant i\leqslant35\}
$$

| Difference set | Triple intersection numbers with multiplicities m = 5 |
| --- | --- |
| DY(-1) | 24^{75}25^{435}26^{1155}27^{2385} … 35^{120} |
| RT(1) | 24^{75}25^{330}26^{1155}27^{2535} … 35^{105} |
| RT(-1) | 24^{90}25^{330}26^{1095}27^{2655} … 35^{120} |

$$
(m=5)
$$

$$
24^{75}25^{435}26^{1155}27^{2385}\cdots35^{120}
$$

$$
24^{75}25^{330}26^{1155}27^{2535}\cdots35^{105}
$$

$$
24^{90}25^{330}26^{1095}27^{2655}\cdots35^{120}
$$

where the exponents denote multiplicities. Since the multiplicities of the (triple) intersection
number 27 are pairwise distinct for the three cases, we conclude that DY(−1), RT(1) and RT(−1)
are pairwise inequivalent when *m* = 5. Hence, the five difference sets *P,* DY(1), DY(−1), RT(1),
and RT(−1) are pairwise inequivalent when *m* = 5. It then follows from Proposition 4.1 that the
skew difference sets RT(1) and RT(−1) are new when *m* = 5.

Based on the above evidence, we make the following conjecture.

**Conjecture 4.3.** *The five difference sets P, DY(1),* DY(−1), RT(1) *and* RT(−1) *in (F*<sub>3</sub>*m, +) are
pairwise inequivalent for all odd m*>*7.*

$$
\left(\mathbb{F}_{3^m},+\right)
$$

$$
m>7
$$

### 5. Difference sets with twin prime power parameters

In this section we present a variation of the classical construction of the twin prime power
difference sets. Using this variation we will show that inequivalent skew Hadamard difference
sets can give rise to inequivalent difference sets with twin prime power parameters. We first recall
the construction of the twin prime power difference sets. As usual, we denote the (multiplicative)
quadratic character of a finite field by *χ.*

$$
\chi
$$

**Theorem 5.1.** (Stanton and Sprott [19]) *Let q and q* + 2 *be odd prime powers. Then the set*
{ ∣} { ∣}
∣ ∣

$$
D=\left\{\left(x,y\right)\mid x\in\mathbb{F}_{q}^{*},y\in\mathbb{F}_{q+2}^{*},\chi\left(x\right)=\chi\left(y\right)\right\}\cup\left\{\left(x,0\right)\mid x\in\mathbb{F}_{q}\right\}
$$

(q+1)2
*is a (4n−* 1,2n− *1,n− 1) difference set in (Fq, +)* × (Fq+2, *+), where n* =.
4

$$
a\left(4n-1,2n-1,n-1\right)
$$

$$
(\mathbb{F}_q,+)\times(\mathbb{F}_{q+2},+)
$$

$$
n=\frac{(q+1)^2}{4}
$$

For a proof of Theorem 5.1, we refer the reader to [19] or [4, p. 354]. For convenience, we
(q+1)2
will refer the parameters *(4n−* 1,2n− *1,n−* 1), *n* =, *q* an odd prime power, as the twin
4
prime power parameters. We now give a variation of the above construction.

$$
(4n-1,2n-1,n-1),n=\frac{(q+1)^{2}}{4},q
$$

**Theorem 5.2.** *Let q and q* + 2 *be prime powers, and let q* ≡ 3 (mod 4
*Hadamard difference set in (F*<sub>q</sub>*, +). Then the set*
{ ∣} { ∣

*). Let E be a skew*
}

$$
q\equiv3
$$

$$
(\mathbb{F}_q,+)
$$

$$
\begin{align*}D=&\left\{\left(x,y\right)\bigm|x\in E,y\in\mathbb{F}_{q+2}^*,\chi\left(y\right)=1\right\}\cup\left\{\left(x,y\right)\bigm|x\in-E,y\in\mathbb{F}_{q+2}^*,\chi\left(y\right)=-1\right\}\\&\cup\left\{\left(x,0\right)\bigm|x\in\mathbb{F}_q\right\}\end{align*}
$$

*is a (4n−* 1,2n− *1,n− 1) difference set in (F*<sub>q</sub>

, +) × (Fq

+2, *+), where n*

<u><em>(q+1)</em></u><sup>2</sup>
*=.*
4

$$
a\left(4n-1,2n-1,n-1\right)
$$

$$
(\mathbb{F}_q,+)\times(\mathbb{F}_{q+2},+)
$$

$$
n=\frac{(q+1)^2}{4}
$$

Noting that the nontrivial character values of a skew Hadamard difference set are given
by (1.1), one can easily give a character theoretic proof for Theorem 5.2. We leave this to the
reader as an exercise.

---

**Remark 5.3.** *(1)* We remark that if *q* and *q* + 2 are both prime powers, and *q* ≡ 1 (mod 4), then
we can similarly use a skew Hadamard difference set in Fq+2to construct a difference set in
*(Fq, +)* × (Fq+2, *+)* with twin prime power parameters.

$$
q\equiv1
$$

$$
q+2
$$

$$
\mathbb{F}_{q+2}
$$

$$
(\mathbb{F}_q,+)\times(\mathbb{F}_{q+2},+)
$$

*(2)* One further generalization of Theorem 5.2 goes as follows. With the assumptions in Theq+1 q−3 q+1
orem 5.2, let *Q* be any *(q* + *2,,,)* partial difference set in (Fq+2, +),0∈/ *Q.* (See
2 4 4
[4, p. 230] for the definition of partial difference set.) Then the set
{ ∣} { ∣} { ∣}

$$
(q+2,\frac{q+1}{2},\frac{q-3}{4},\frac{q+1}{4})
$$

$$
(\mathbb{F}_{q+2},+),0\notin Q
$$

$$
D^{\prime}=\left\{(x,y)\mid x\in E,y\in Q\right\}\cup\left\{(x,y)\mid x\in-E,y\in\mathbb{F}_{q+2}^{*}\setminus Q\right\}\cup\left\{(x,0)\mid x\in\mathbb{F}_{q}\right\}
$$

is a *(4n−* 1,2n− *1,n− 1)* difference set in *(F*<sub>q</sub>*, +)*

× (Fq+2, +), where *n*

<u><em>(q+1)</em></u><sup>2</sup>
=.
4

$$
(4n-1,2n-1,n-1)
$$

$$
(\mathbb{F}_q,+)\times(\mathbb{F}_{q+2},+)
$$

$$
n=\frac{(q+1)^2}{4}
$$

In view of the fact that there exist inequivalent skew Hadamard difference sets in *(F*<sub>q</sub>*,* +), the
following theorem is of interest.

$$
(\mathbb{F}_q,+)
$$

**Theorem 5.4.** *Let q and q* + 2 *be prime powers, and let q* ≡ 3 (mod *4). Let E and F be inequivalent skew Hadamard difference sets in (F*<sub>q</sub>*, +). Then the two difference sets*
{ ∣} { ∣}

$$
q+2
$$

$$
q\equiv3\pmod{4}
$$

$$
(\mathbb{F}_q,+)
$$

$$
\begin{align*}D=&\left\{\left(x,y\right)\bigm|x\in E,y\in\mathbb{F}_{q+2}^*,\chi\left(y\right)=1\right\}\cup\left\{\left(x,y\right)\bigm|x\in-E,y\in\mathbb{F}_{q+2}^*,\chi\left(y\right)=-1\right\}\\&\cup\left\{\left(x,0\right)\bigm|x\in\mathbb{F}_q\right\}\end{align*}
$$

*and*

$$
\begin{align*}D'=&\left\{\left(x,y\right)\bigm|x\in F,y\in\mathbb{F}_{q+2}^*,\chi\left(y\right)=1\right\}\cup\left\{\left(x,y\right)\bigm|x\in-F,y\in\mathbb{F}_{q+2}^*,\chi\left(y\right)=-1\right\}\\&\cup\left\{\left(x,0\right)\bigm|x\in\mathbb{F}_q\right\}\end{align*}
$$

*are inequivalent.*

**Proof.** Assume that *D* and *D<sup>′</sup>* are equivalent difference sets in
there exists an automorphism *α* of *G* and an element

*G* = *(F*<sub>q</sub>*, +)
(b*<sub>1</sub>*, b*<sub>2</sub>*)* ∈ *G* such that

× (F<sub>q</sub>+2, +). Then

$$
D'
$$

$$
G=(\mathbb{F}_q,+)\times(\mathbb{F}_{q+2},+)
$$

$$
(b_{1},b_{2})\in G
$$

$$
\alpha(D)=D^{\prime}+(b_{1},b_{2}).
$$

(5.1)

We will show that *E* and *F* are equivalent.

For convenience, we define
{ ∣

$$
\begin{aligned}&A_{1}=\left\{\left(x,y\right)\bigm|x\in E,y\in\mathbb{F}_{q+2}^{*},\chi\left(y\right)=1\right\}\cup\big\{\left(x,y\right)\bigm|x\in-E,y\in\mathbb{F}_{q+2}^{*},\chi\left(y\right)=-1\big\},\\&A_{2}=\left\{\left(x,y\right)\bigm|x\in F,y\in\mathbb{F}_{q+2}^{*},\chi\left(y\right)=1\right\}\cup\big\{\left(x,y\right)\bigm|x\in-F,y\in\mathbb{F}_{q+2}^{*},\chi\left(y\right)=-1\big\},\\ \end{aligned}
$$

and

$$
B=\left\{(x,0)\mid x\in\mathbb{F}_q\right\}.
$$

$$
D=A_{1}\cup B,D^{\prime}=A_{2}\cup B
$$

′
So *D* = *A*<sub>1</sub>∪ *B, D* = *A*<sub>2</sub>∪ *B,* and (5.1) can be written as
() ()

$$
\alpha\left(A_{1}\right)\cup\alpha\left(B\right)=\left(A_{2}+\left(b_{1},b_{2}\right)\right)\cup\left(B+\left(b_{1},b_{2}\right)\right).
$$

(5.2)

Since *gcd(q, q* + *2)* = 1, we have Aut
*f* ∈ Aut(Fq, *+)* and *g* ∈ Aut(Fq+2, +
We claim that *b*<sub>2</sub>= 0. If not, then there exists a
*B +(b*<sub>1</sub>*, b*<sub>2</sub>*)* = {*(x, b*<sub>2</sub>*)* | *x* ∈ F<sub>q</sub>
{() ∣} {

*(G)* ∼ (
= Aut
) such that *α(x,y)*
}. By (5.2), we must have
∣}

Fq, +) × Aut(Fq+2, +
= *(f (x), g(y))* for all
∗
*y* ∈ F such that
q+2

*).* Hence there exist
*(x, y)* ∈ *G.
g(y)* = *b*<sub>2</sub>. Note that

$$
\gcd(q,q+2)=1
$$

$$
\mathrm{Aut}(G)\cong\mathrm{Aut}(\mathbb{F}_q,+)\times\mathrm{Aut}(\mathbb{F}_{q+2},+)
$$

$$
f\in\mathrm{Aut}(\mathbb{F}_q,+)
$$

$$
g\in\mathrm{Aut}(\mathbb{F}_{q+2},+)
$$

$$
\alpha(x,y)=(f(x),g(y))
$$

$$
(x,y)\in G
$$

$$
b_{2}=0.
$$

$$
y\in\mathbb{F}_{q+2}^{*}
$$

$$
g(y)=b_2
$$

$$
B+\left(b_{1},b_{2}\right)=\left\{\left(x,b_{2}\right)\mid x\in\mathbb{F}_{q}\right\}
$$

$$
\left\{\left(f\left(x\right),g\left(y\right)\right)\mid x\in E\right\}=\left\{\left(x,b_{2}\right)\mid x\in\mathbb{F}_{q}\right\},
$$ or

$$
\left\{\left(f\left(x\right),g\left(y\right)\right)\mid x\in-E\right\}=\left\{\left(x,b_{2}\right)\mid x\in\mathbb{F}_{q}\right\},
$$

according as *χ(y)=* 1 *orχ(y)=* −1. However both equalities are clearly impossible by comparing the cardinalities of the sets involved. This proves that *b*<sub>2</sub>= 0. It follows that *α(B)* =
*B +(b*<sub>1</sub>*,0)* and

$$
\chi(y)=1or\chi(y)=-1
$$

$$
\alpha(B)=
b_{2}=0
$$

$$
B+(b_1,0)
$$

$$
\alpha(A_{1})=A_{2}+(b_{1},0).
$$

(5.3)

∗
Let *y* ∈ F such that *g(y)* = 1. From (5.3), we see that
q+2
{() ∣} { ∣}

$$
y\in\mathbb{F}_{q+2}^*
$$

$$
g(y)=1
$$

$$
\left\{\left(f\left(x\right),g\left(y\right)\right)\mid x\in E\right\}=\left\{\left(x+b_{1},1\right)\mid x\in F\right\},
$$

or

$$
\left\{\left(f\left(x\right),g\left(y\right)\right)\mid x\in-E\right\}=\left\{\left(x+b_{1},1\right)\mid x\in F\right\},
$$

according to *χ(y)=* 1 *orχ(y)*
*E* and *F* are equivalent difference sets in

= −1. So *f (E)= F
(F*<sub>q</sub>*,* +).

+ *b*<sub>1</sub>or *−f (E)= F* + *b*<sub>1</sub>. This proves that
✷

$$
\chi\left(y\right)=1{\mathrm{~o r~}}\chi\left(y\right)=-1.{\mathrm{~S o~}}f(E)=F+b_{1}{\mathrm{~o r~}}{-f(E)}=F+b_{1}
$$

$$
(\mathbb{F}_q,+).\quad\square
$$

2h+1
Combining Theorem 5.4 with the results in Section 4, we see that whenever 3 ± 2 (*h*>1)
is a prime power, there exist difference sets with twin prime power parameters that are inequivalent to the classical twin prime power difference sets. To indicate that there are *h*>1 such that
2h+1 5
3 ± 2 are prime powers, we mention the following specific examples: 3 −2= 241 is a
prime, 3<sup>9</sup> −2= 19 681 is a prime, and 3<sup>15</sup> +2= 14 348 909 is also a prime.

$$
3^{2h+1}\pm2(h>1)
$$

$$
h>1
$$

$$
3^{2h+1}\pm2
$$

$$
3^{5}-2=241
$$

$$
3^{9}-2=19681
$$

$$
3^{15}+2=14348909
$$

### Acknowledgment

The authors thank an anonymous referee for his/her helpful comments.

### Appendix A

In this appendix, we give the promised proof of (3.8). Throughout this section, *m* = 2h+ 1 is
m+1m+1
m2r
a positive odd integer, *q* = 3, *r* = = *h+* 1, and *α* = 3 = 3. Our goal is to prove
2

$$
m=2h+1
$$

$$
q=3^{m},r=\frac{m+1}{2}=h+1
$$

$$
\alpha=3^{\frac{m+1}{2}}=3^{r}
$$

**Theorem A.1.** *For each a,0*
(

*a q* − *2, we have*
)

$$
a,0\leqslant a\leqslant q-2
$$

$$
s(a)+s\left(\frac{q-1}{2}-a(\alpha+2)\right)\geqslant m,
$$

(A.1)

*where s(a) is the digit sum of a defined in Section*

*1.*

First of all, we observe that the only

a,0 *a q*

− 2, satisfying

$$
a,0\leqslant a\leqslant q-2
$$

$$
\frac{q-1}{2}-a(\alpha+2)\equiv0\pmod{q-1}
$$

q−1 q−1 q−
is *a* =. Fora =, we *haves(a)* = *m* and *s(* − *a(α* + *2))* = 0. So certainly (A.1)
2 2 2 1
q−1 q−1
holds for *a* =. Therefore in our discussion below, we will always assume that *a* (and
2 2
<sub>q</sub>−1=
*−a(α* + *2)*
2
≡ 0 (mod *q* − 1)).

$$
a=\frac{q-1}{2}
$$

$$
a=\frac{q-1}{2}
$$

$$
s(a)=m
$$

$$
s\left(\frac{q-1}{2}-a(\alpha+2)\right)=0
$$

$$
a=\frac{q-1}{2}
$$

$$
a\neq\frac{q-1}{2}
$$

$$
\frac{q-1}{2}-a(\alpha+2)\not\equiv0\pmod{q-1}
$$

---

A sequence {*u*<sub>i</sub>}<sub>i</sub><sub>∈Z</sub>is called periodic with period *m* if *u*<sub>i</sub>= *u*<sub>j</sub>whenever *i* ≡ *j* (mod *m).* All
sequences in this section are periodic with period *m.* Leta be an integer satisfying 0 *a q* − 2
q−1
and *a.* Write
2
=

$$
\{u_{i}\}_{i\in\mathbb{Z}}
$$

$$
u_{i}=u_{j}
$$

$$
i\equiv j
$$

$$
0\leqslant a\leqslant q-2
$$

$$
a\neq\frac{q-1}{2}
$$

$$
a=\sum_{i=0}^{m-1}a_{i}3^{i},\quad a_{i}\in\{0,1,2\},
$$

and extend *a0, a1,...,am−1to* a periodic sequence with period *m.* We have

$$
a_{0},a_{1},\ldots,a_{m-1}
$$

$$
\begin{align*}\frac{q-1}{2}-\big(3^r+2\big)a&=\frac{q-1}{2}-3^ra-3a+a\\&\equiv\sum_{i=0}^{m-1}(1-a_{i-r}-a_{i-1}+a_i)3^i\pmod{3^m-1}\\&\equiv\sum_{i=0}^{m-1}\big(1+(2-a_{i-r})+(2-a_{i-1})+a_i\big)3^i\pmod{3^m-1}\\&=\sum_{i=0}^{m-1}(5+a_i-a_{i-1}-a_{i-r})3^i.\end{align*}
$$

For each *i,* let

$$
b_{i}=5+a_{i}-a_{i-1}-a_{i-r}.
$$

It is easily seen that *b*<sub>i</sub>∈ {*1,2,3,...,7}.* Write

$$
b_{i}\in\{1,2,3,\ldots,7\}
$$

$$
\sum_{i=0}^{m-1}b_{i}3^{i}\equiv\sum_{i=0}^{m-1}s_{i}3^{i}\pmod{3^{m}-1}
$$

with *s*<sub>i</sub>∈ {0,1,2}. By Theorem 13 of [10] (adapted to the ternary case), there exists a sequence
{*c*<sub>i</sub>} such that

$$
s_{i}\in\{0,1,2\}
$$

$$
\left\{c_{i}\right\}
$$

$$
\forall i,\quad s_{i}=b_{i}-3c_{i}+c_{i-1},
$$

(A.2)

where *c*<sub>i</sub>∈ {0,1,2,3} is the carry from the ith digit to the *(i* + 1)th digit in the modular summaq−1 r
tion of, <u>−3</u> a, −3a and a. Note that
2
()

$$
c_{i}\in\{0,1,2,3\}
$$

$$
\frac{q-1}{2},-3^{r}a,-3a
$$

$$
\begin{align*}s(a)+s\Biggl(\frac{q-1}{2}-\bigl(3^r+2\bigr)a\Biggr)&=\sum_{i=0}^{m-1}a_i+\sum_{i=0}^{m-1}\bigl((5+a_i-a_{i-1}-a_{i-r})-3c_i+c_{i-1}\bigr)\\&=5m-2\sum_{i=0}^{m-1}c_i.\end{align*}
$$

So in order to prove Theorem A.1, it suffices to prove

$$
\sum_{i=0}^{m-1}c_{i}\leqslant2m.
$$

(A.3)

Since *gcd(r, m)* = *gcd(r,2r* − *1)* = 1, for any fixed *i,* the sequence *ci, c*<sub>i</sub>*−r, c*<sub>i</sub><sub>−</sub>*2r,...,
c*<sub>i</sub><sub>−</sub><sub>(m</sub>−1)ris a rearrangement of *c0, c*<sub>1</sub>*,...,c*<sub>m</sub>−1. In the following, we will also frequently use
the facts that *2r* ≡ 1 (mod *m), c*<sub>i</sub>−1= *c*<sub>i</sub><sub>−2</sub>*r, c*<sub>i</sub>−2= *c*<sub>i</sub><sub>−4</sub>*r,* and so on.

$$
\gcd(r,m)=\gcd(r,2r-1)=1
$$

$$
c_{l},c_{l-r},c_{l-2r},\ldots,
$$

$$
c_{i-(m-1)r}
$$

$$
c_{0},c_{1},\ldots,c_{m-1}
$$

$$
2r\equiv1\pmod{m},c_{i-1}=c_{i-2r},c_{i-2}=c_{i-4r}
$$

---

$$
If c_{i}=3
$$

**Lemma A.2.** *If c*<sub>i</sub>= *3, then c*

<sub>i</sub>−1= 2 *and* ci−r2, ai= *2, a*<sub>i</sub>−1= *a*<sub>i</sub><sub>−</sub>*r= 0.*

$$
c_{i-1}=2
$$

$$
c_{i-r}\leqslant2,a_i=2,a_{i-1}=a_{i-r}=0.
$$

**Proof.** Note that *s*<sub>i</sub>= *b*<sub>i</sub>

− *3c*<sub>i</sub>+ *c*<sub>i</sub><sub>−1</sub>0, 1 *b*<sub>i</sub>7, 0 *c*<sub>i</sub><sub>−1</sub>3. If *c*<sub>i</sub>= 3, then

$$
s_{i}=b_{i}-3c_{i}+c_{i-1}\geqslant0,1\leqslant b_{i}\leqslant7,0\leqslant c_{i-1}\leqslant3.
$$

$$
c_{i}=3
$$

$$
6\leqslant b_{i}\leqslant7,\quad2\leqslant c_{i-1}\leqslant3.
$$

(A.4)

Assume to the contrary that

ci−1= 3. Since

$$
c_{i-1}=3
$$

$$
s_{i-1}=b_{i-1}-3c_{i-1}+c_{i-2}\geqslant0,
$$

we have

(A.5)

$$
6\leqslant b_{i-1}\leqslant7,\quad2\leqslant c_{i-2}\leqslant3.
$$

From the lower bounds on

*b*<sub>i</sub>and *b*<sub>i</sub><sub>−1</sub>in (A.4) and (A.5), we have

$$
b_{i}
$$

$$
b_{i-1}
$$

$$
\begin{aligned}&6\leqslant b_{i}=5+a_{i}-a_{i-1}-a_{i-r},\quad and\\&6\leqslant b_{i-1}=5+a_{i-1}-a_{i-2}-a_{i-r-1}.\\ \end{aligned}
$$

Adding up the two inequalities, we get

$$
10+a_{i}-a_{i-r}-a_{i-2}-a_{i-r-1}\geqslant12,
$$

which implies that

$$
a_{i}=2,\qquad a_{i-r}=a_{i-r-1}=a_{i-2}=0.
$$

We use the following table to summarize the above information:
[]

$$
\mathrm{A}:=\begin{bmatrix}a_{i}&a_{i-r}&a_{i-1}&a_{i-r-1}&a_{i-2}\\ 2&0&\geqslant0&0&0\end{bmatrix}.
$$

Since

$$
b_{i}=5+a_{i}-a_{i-1}-a_{i-r}\geqslant6,
$$

using the information in Table A, we have

$$
a_{i-1}\leqslant1.
$$

Since

$$
b_{i-1}=5+a_{i-1}-a_{i-2}-a_{i-r-1}\geqslant6,
$$

again using the information in Table A, we have

$$
a_{i-1}\geqslant1.
$$

$$
a_{i-1}=1
$$

Hence *a*<sub>i</sub><sup>−1</sup>= 1. Therefore we can update the entries in Table A as follows:
[]

$$
\mathrm{A}=\left[\begin{matrix}{a_{i}}&{a_{i-r}}&{a_{i-1}}&{a_{i-r-1}}&{a_{i-2}}\\ {2}&{0}&{1}&{0}&{0}\\ \end{matrix}\right].
$$

It follows that *b*<sub>i</sub>−1=5+a<sub>i</sub>−1− *a*<sub>i</sub>−2−
*c*<sub>i</sub><sub>−1</sub>= 3, we have *c*<sub>i</sub><sub>−2</sub>= 3. Combining this with
*b*<sub>i</sub><sub>−2</sub>6.

ai−r−1= 6. Since *s*<sub>i</sub>−1= *b*<sub>i</sub>−1− *3c*<sub>i</sub>−1+ *c*<sub>i</sub><sub>−2</sub>0 and
*s*<sub>i</sub><sub>−2</sub>= *b*<sub>i</sub><sub>−2</sub>− *3c*<sub>i</sub><sub>−2</sub>+ *c*<sub>i</sub><sub>−3</sub>0, we obtain

$$
b_{i-1}=5+a_{i-1}-a_{i-2}-a_{i-r-1}=6
$$

$$
s_{i-1}=b_{i-1}-3c_{i-1}+c_{i-2}\geqslant0
$$

$$
c_{i-1}=3
$$

$$
c_{i-2}=3
$$

$$
s_{i-2}=b_{i-2}-3c_{i-2}+c_{i-3}\geq0
$$

$$
b_{i-2}\geqslant6
$$

---

Since

$$
b_{i-1}=5+a_{i-1}-a_{i-2}-a_{i-r-1}\geqslant6,
$$

$$
b_{i-2}=5+a_{i-2}-a_{i-3}-a_{i-r-2}\geqslant6,
$$

adding up these two inequalities, we get

$$
10+a_{i-1}-a_{i-r-1}-a_{i-3}-a_{i-r-2}\geqslant12,
$$

which implies that

$$
a_{i-1}=2,\qquad a_{i-r-1}=a_{i-3}=a_{i-r-2}=0.
$$

But this is in contradiction with the previous conclusion that *a*<sub>i</sub><sub>−1</sub>= 1 as shown in Table A.
Hence *ci−1* i−1= 2.

$$
a_{i-1}=1
$$

$$
c_{i-1}\neq3
$$

$$
c_{i-1}=2
$$

Combining the fact = 3. By (A.4) we must have *c*<sub>i</sub><sub>−1</sub>= 2,
that

*c*<sub>i</sub>= 3 with *c s*<sub>i</sub>= *b*<sub>i</sub>− *3c*<sub>i</sub>+ *c*<sub>i</sub><sub>−1</sub>0, we have *b*<sub>i</sub>= 7. Recall

$$
c_{i-1}=2,\;c_i=3
$$

$$
s_{i}=b_{i}-3c_{i}+c_{i-1}\geqslant0
$$

$$
b_{i}=7
$$

$$
b_{i}=5+a_{i}-a_{i-1}-a_{i-r}\leqslant7.
$$

We obtain

$$
a_{i}=2,\quad a_{i-1}=a_{i-r}=0.
$$

Now *b*<sub>i</sub><sub>−</sub>r=5+a<sub>i</sub><sub>−</sub>*r− a*<sub>i</sub><sub>−</sub><sub>r</sub>−1
c<sub>i</sub>−<sub>r</sub><sub>−</sub>13, we conclude that *c*<sub>i</sub>

− *a*<sub>i</sub>−1=5−a<sub>i</sub><sub>−</sub><sub>r</sub><sub>−1</sub>5, *s*<sub>i</sub><sub>−</sub>*r= b*<sub>i</sub><sub>−</sub>*r− 3c*<sub>i</sub><sub>−</sub>*r+ c*<sub>i</sub><sub>−</sub><sub>r</sub><sub>−1</sub>0, and
−r2. This completes the proof. ✷

$$
\mathrm{low}\;b_{i-r}=5+a_{i-r}-a_{i-r-1}-a_{i-1}=5-a_{i-r-1}\leqslant5,s_{i-r}=b_{i-r}-3c_{i-r}+c_{i-r-1}\geqslant0,\varepsilon
$$

$$
c_{i-r-1}\leqslant3
$$

$$
c_{i-r}\leqslant2
$$

**Lemma A.3.** *If* ci= *3,* ci−r= *c*
[]

i−1= *2, then c*<sub>i</sub><sub>−</sub><sub>r</sub><sup>−1</sup>*2. That is,*
[]

$$
I f c_{i}=3,c_{i-r}=c_{i-1}=2
$$

$$
c_{i-r-1}\leqslant2.
$$

$$
\begin{bmatrix}c_{i}&c_{i-r}&c_{i-1}\\ 3&=2&=2\end{bmatrix}\quad\Rightarrow\quad\begin{bmatrix}c_{i}&c_{i-r}&c_{i-1}&c_{i-r-1}\\ 3&=2&=2&\leqslant2\end{bmatrix}.
$$

**Proof.** Assume to the contrary that
*a*<sub>i</sub><sub>−</sub><sub>r</sub>−1= 2, and *a*<sub>i</sub><sub>−</sub><sub>r</sub>−2= *a*<sub>i</sub>−2

*c*<sub>i</sub><sub>−</sub><sub>r</sub>−1= 3. By Lemma A.2, we have *c*<sub>i</sub><sub>−</sub><sub>r</sub>−2= 2, *c*<sub>i</sub><sub>−2</sub>2,
= 0. Since

$$
c_{i-r-1}=3
$$

$$
c_{i-r-2}=2,c_{i-2}\leqslant2,
$$

$$
a_{i-r-1}=2
$$

$$
a_{i-r-2}=a_{i-2}=0
$$

$$
s_{i-1}=b_{i-1}-3c_{i-1}+c_{i-2}\geqslant0,
$$

and *c*<sub>i</sub><sub>−1</sub>= 2, *c*<sub>i</sub><sub>−2</sub>2, we have *b*<sub>i</sub><sub>−1</sub>4. By assumption *c*<sub>i</sub>= 3. It follows from Lemma A.2
that ai= 2, *a*<sub>i</sub>−1= *a*<sub>i</sub><sub>−</sub>*r=* 0. We use the following table to summarize the above information:
[]

$$
c_{i-1}=2,\quad c_{i-2}\leqslant2
$$

$$
b_{i-1}\geqslant4
$$

$$
c_{i}=3
$$

$$
a_{i}=2,a_{i-1}=a_{i-r}=0
$$

$$
\mathrm{A}:=\begin{bmatrix}a_{i}&a_{i-r}&a_{i-1}&a_{i-r-1}&a_{i-2}&a_{i-r-2}\\ 2&0&0&2&0&0\end{bmatrix}.
$$

$$
b_{i-1}=5+a_{i-1}-a_{i-2}-a_{i-r-1}.
$$

Recall that

Using theinformation in Table A, we have
previous conclusion that *b*<sub>i</sub><sub>−1</sub>

*b*<sub>i</sub><sub>−1</sub>=5+0−0−2= 3, which contradicts the
4. This completes the proof. ✷

$$
b_{i-1}=5+0-0-2=3
$$

$$
b_{i-1}\geqslant4
$$

**Theorem A.4.** *Let t* 3
*a*<sub>i</sub><sub>−</sub><sub>r</sub>*1, a*<sub>i</sub><sub>−2</sub><sub>r</sub>*1,..., a*<sub>i</sub><sub>−</sub><sub>(t</sub><sub>−1</sub>
*if* ci= *3, c*<sub>i</sub>−r= *c*<sub>i</sub><sub>−</sub>2r=···=
*ai−tr1.*

*be an integer. If c*<sub>i</sub>= *3, c*<sub>i</sub>
*)r1, ai−(t−2)r+ a
ci*<sub>−</sub>tr= 2 *and also c*

−r= ci−2r=···=ci−tr
*i−(t−1)r1, and ci−tr−r*
<sub>i</sub>−<sub>tr</sub><sub>−</sub>r= *2, then* ai−tr

= *2, then a*<sub>i</sub>= *2,*
*2. Furthermore,*
1 *and ai−(t−1)r+*

$$
t\geqslant3
$$

$$
\begin{align*}if c_i=3,c_{i-r}=c_{i-2r}=\cdots=c_{i-tr}=2,\end{align*}
$$

$$
a_{i}=2_{,}
$$

$$
a_{i-r}\leqslant1,a_{i-2r}\leqslant1,\ldots,a_{i-(t-1)r}\leqslant1,a_{i-(t-2)r}+a_{i-(t-1)r}\leqslant1
$$

$$
c_{i-tr-r}\leqslant2
$$

$$
c_{i}=3,\ c_{i-r}=c_{i-2r}=\cdots=c_{i-tr}=2
$$

$$
c_{i-tr-r}=2
$$

$$
a_{i-tr}\leqslant1
$$

$$
a_{i-(t-1)r}+
a_{i-tr}\leqslant1
$$

---

**Proof.** We will use induction on
*c*<sub>i</sub><sub>−3</sub>*r=* 2 (i.e.,c<sub>i</sub><sub>−</sub>*r= c*<sub>i</sub><sub>−1</sub>
*ai−r+* ai−11, and *ci−3r*

*t.* When *t* = 3, the assumptions are
= ci−r−1= 2). We will show that *a*
−r= ci−22.

ci= 3, and *c*<sub>i</sub>−r= *c*<sub>i</sub><sub>−</sub>2r=
*i=* 2,a<sub>i</sub><sub>−</sub><sub>r</sub>1,a<sub>i</sub><sub>−2</sub>*r= a*<sub>i</sub><sub>−1</sub>1,

$$
c_{i}=3
$$

$$
c_{i-r}=c_{i-2r}=
c_{i-3r}=2\left(\mathrm{i.e.},c_{i-r}=c_{i-1}=c_{i-r-1}=2\right)
$$

$$
a_{i}=2,a_{i-r}\leqslant1,a_{i-2r}=a_{i-1}\leqslant1
$$

$$
c_{i-3r-r}=c_{i-2}\leqslant2
$$

$$
a_{i-r}+a_{i-1}\leqslant1
$$

Since *c*<sub>i</sub>= 3, by Lemma A.2, we have

$$
c_{i}=3
$$

$$
a_{i}=2,\quad a_{i-r}=0,\quad a_{i-1}=0.
$$

(A.6)

It remains to show that ci−22. Assume to the contrary that ci−2= 3, by Lemma A.2, we have
ci−3= 2 and *c*<sub>i</sub><sub>−2−</sub>r2, *a*<sub>i</sub><sub>−2</sub>= 2, *a*<sub>i</sub><sub>−3</sub>= *a*<sub>i</sub><sub>−2−</sub>*r=* 0. We summarize the information in the
following table:
[]

$$
c_{i-2}\leqslant2
$$

$$
c_{i-2}=3
$$

$$
c_{i-2-r}\leqslant2,a_{i-2}=2,a_{i-3}=a_{i-2-r}=0
$$

$$
c_{i-3}=2
$$

$$
\mathbf{A}:=\left[\begin{matrix}{a_{i}}&{a_{i-r}}&{a_{i-1}}&{a_{i-r-1}}&{a_{i-2}}&{a_{i-r-2}}&{a_{i-3}}\\ {2}&{0}&{0}&{\leqslant2}&{2}&{0}&{0}\\ \end{matrix}\right].
$$

Since

$$
s_{i-r-1}=b_{i-r-1}-3c_{i-r-1}+c_{i-r-2}\geqslant0,
$$

$$
s_{i-1}=b_{i-1}-3c_{i-1}+c_{i-2}\geqslant0,
$$

$$
c_{i-r-1}=2,\qquad c_{i-r-2}\leqslant2,\qquad c_{i-1}=2,\qquad c_{i-2}=3,
$$

we see that *b*<sub>i</sub><sub>−</sub><sub>r</sub><sub>−1</sub>4 and

*b*<sub>i</sub><sub>−1</sub>3. Using the information in Table A, we find that

$$
b_{i-r-1}\geqslant4
$$

$$
b_{i-1}\geqslant3
$$

$$
b_{i-r-1}=5+a_{i-r-1}-a_{i-r-2}-a_{i-2}=3+a_{i-r-1}.
$$

So *b*<sub>i</sub><sub>−</sub><sub>r</sub><sub>−1</sub>4 implies that

*a*<sub>i</sub><sub>−</sub><sub>r</sub><sub>−1</sub>1. Again using the information in Table A, we find that

$$
b_{i-r-1}\geqslant4
$$

$$
a_{i-r-1}\geqslant1
$$

$$
b_{i-1}=5+a_{i-1}-a_{i-2}-a_{i-r-1}=3-a_{i-r-1}.
$$

$$
b_{i-1}\geqslant3
$$

So *b*<sub>i</sub><sub>−1</sub>3 implies that
*a*<sub>i</sub><sub>−</sub><sub>r</sub><sub>−1</sub>1. Therefore we must have

*a*<sub>i</sub><sub>−</sub><sub>r</sub><sub>−1</sub>0, which contradicts with the previous conclusion that
*c*<sub>i</sub><sub>−2</sub>2.

$$
a_{i-r-1}\leqslant0
$$

$$
a_{i-r-1}\geqslant1
$$

$$
c_{i-2}\leqslant2
$$

Next we show that if
ci−<sub>r</sub>−1= *c*<sub>i</sub><sub>−</sub>2= 2), then *a*
true. Since

ci= 3 and *c*<sub>i</sub>−r= *c*<sub>i</sub><sub>−</sub>2r= *c*<sub>i</sub><sub>−3</sub>*r= c*<sub>i</sub><sub>−4</sub>*r=* 2 (i.e.,c<sub>i</sub><sub>−</sub>*r= c*<sub>i</sub><sub>−1</sub>=
i−3r= ai−r−11, and ai−1+ ai−r−11. Note that (A.6) is still

$$
c_{i}=3
$$

$$
c_{i-r}=c_{i-2r}=c_{i-3r}=c_{i-4r}=2\quad(i.e.,\quad c_{i-r}=c_{i-1}=
c_{i-r-1}=c_{i-2}=2
$$

$$
a_{i-3r}=a_{i-r-1}\leqslant1
$$

$$
a_{i-1}+a_{i-r-1}\leqslant1
$$

$$
s_{i-r}=b_{i-r}-3c_{i-r}+c_{i-r-1}\geqslant0,
$$

$$
s_{i-1}=b_{i-1}-3c_{i-1}+c_{i-2}\geqslant0,
$$

$$
c_{i-r}=c_{i-1}=c_{i-r-1}=c_{i-2}=2,
$$

we have

$$
4\leqslant b_{i-r}=5+a_{i-r}-a_{i-r-1}-a_{i-1},
$$

(A.7)

$$
4\leqslant b_{i-1}=5+a_{i-1}-a_{i-2}-a_{i-r-1}.
$$

(A.8)

Adding up (A.7) and (A.8), we get

$$
10+a_{i-r}-2a_{i-r-1}-a_{i-2}\geqslant8.
$$

As ai−r= 0 (see (A.6)), the above inequality becomes

$$
a_{i-r}=0(see(A.6))
$$

$$
2a_{i-r-1}+a_{i-2}\leqslant2.
$$

Since *a*<sub>i</sub><sub>−2</sub>0, we have

$$
a_{i-2}\geqslant0
$$

$$
a_{i-r-1}\leqslant1.
$$

---

$$
a_{i-1}=0
$$

Noting that ai−1

= 0 (see (A.6)), we have

$$
a_{i-1}+a_{i-r-1}\leqslant1.
$$

This finishes the proof in the case where

*t* = 3.

$$
t=3
$$

Assume that the theorem is proved for
assume that *c*<sub>i</sub>= 3,

*c*<sub>i</sub><sub>−</sub>*r= c*<sub>i</sub><sub>−2</sub>*r*

*t* = *k* − 1 3. We will prove the theorem for *t* = *k.* So
=···=ci−kr= 2. By induction hypothesis, we have

$$
t=k-1\geqslant3
$$

$$
t=k
$$

$$
c_{i}=3,c_{i-r}=c_{i-2r}=\cdots=c_{i-kr}=2
$$

$$
\begin{aligned}&a_{i}=2,\qquad a_{i-r}\leqslant1,\qquad a_{i-2r}\leqslant1,\qquad\ldots,\qquad a_{i-(k-2)r}\leqslant1,\\&a_{i-(k-3)r}+a_{i-(k-2)r}\leqslant1.\\ \end{aligned}
$$

(A.9)

Since it is also assumed that

*c*<sub>i</sub><sub>−</sub>*kr*

= 2, we have

$$
c_{i-kr}=2
$$

(A.10)

$$
a_{i-(k-1)r}\leqslant1,\qquad a_{i-(k-2)r}+a_{i-(k-1)r}\leqslant1.
$$

Now we show that *c*<sub>i</sub><sub>−</sub><sub>kr</sub><sub>−</sub>r2. Assume to the contrary that *c*<sub>i</sub>−<sub>kr</sub>−r= 3. Then by Lemma A.2,
we have *c*<sub>i</sub>−<sub>kr</sub>−r−1= 2, *c*<sub>i</sub><sub>−</sub><sub>kr</sub>−12, and *a*<sub>i</sub>−<sub>kr</sub><sub>−</sub>r= 2, *a*<sub>i</sub>−kr−r−1= *a*<sub>i</sub><sub>−</sub><sub>kr</sub>−1= 0. As before we
summarize the information in the following table:
[]

$$
c_{i-kr-r}\leqslant2
$$

$$
c_{i-kr-r}=3
$$

$$
c_{i-kr-r-1}=2,\quad c_{i-kr-1}\leq2
$$

$$
a_{i-kr-r}=2,\;a_{i-kr-r-1}=a_{i-kr-1}=0
$$

$$
\mathbb{B}:=\left[\begin{matrix}{a_{i-(k-2)r}}&{a_{i-(k-1)r}}&{a_{i-k r}}&{a_{i-k r-r}}&{a_{i-k r-1}}&{a_{i-k r-r-1}}\\ {\leqslant1}&{\leqslant1}&{\geqslant0}&{2}&{0}&{0}\\ \end{matrix}\right].
$$

Since

$$
s_{i-(k-1)r}=b_{i-(k-1)r}-3c_{i-(k-1)r}+c_{i-k r-r}\geqslant0,
$$

$$
s_{i-kr}=b_{i-kr}-3c_{i-kr}+c_{i-kr-1}\geqslant0,
$$

$$
c_{i-(k-1)r}=c_{i-kr}=2,\qquad c_{i-kr-r}=3,\qquad c_{i-kr-1}\leqslant2;
$$

we have

$$
3\leqslant b_{i-(k-1)r}=5+a_{i-(k-1)r}-a_{i-kr-r}-a_{i-kr},
$$

(A.11)

$$
4\leqslant b_{i-kr}=5+a_{i-kr}-a_{i-kr-1}-a_{i-kr-r}.
$$

(A.12)

Adding up (A.11) and (A.12), we get

$$
10+a_{i-(k-1)r}-2a_{i-k r-r}-a_{i-k r-1}\geqslant7.
$$

Since *a*<sub>i</sub>−<sub>kr</sub>−r

= 2, we have

$$
a_{i-kr-r}=2
$$

$$
a_{i-(k-1)r}-a_{i-kr-1}\geqslant1,
$$

which implies that
we have

ai−(k−1)r1. Combining this with the information on

*a*<sub>i</sub><sub>−</sub><sub>(k</sub>−1)rin Table B,

$$
a_{i-(k-1)r}\geqslant1
$$

$$
a_{i-(k-1)r}
$$

(A.13)

$$
a_{i-(k-1)r}=1.
$$

Thus we can update the information in Table B as follows:
[

$$
\mathbb{B}=\begin{bmatrix}a_{i-(k-2)r}&a_{i-(k-1)r}&a_{i-k r}&a_{i-k r-r}&a_{i-k r-1}&a_{i-k r-r-1}\\ \leqslant1&=1&\geqslant0&2&0&0\end{bmatrix}.
$$

Using the updated Table B and (A.11) (respectively, (A.12)), we get
*a*<sub>i</sub><sub>−</sub><sub>kr</sub>1). Hence

*a*<sub>i</sub><sub>−</sub><sub>kr</sub>1 (respectively,

$$
a_{i-kr}\leqslant1
$$

$$
a_{i-kr}\geqslant1
$$

$$
a_{i-kr}=1.
$$

(A.14)

---

Since

$$
s_{i-(k-3)r}=b_{i-(k-3)r}-3c_{i-(k-3)r}+c_{i-(k-1)r}\geqslant0,
$$

$$
s_{i-(k-2)r}=b_{i-(k-2)r}-3c_{i-(k-2)r}+c_{i-kr}\geqslant0,
$$

$$
c_{i-(k-3)r}=c_{i-(k-2)r}=c_{i-(k-1)r}=c_{i-kr}=2;
$$

we have

$$
4\leqslant b_{i-(k-3)r}=5+a_{i-(k-3)r}-a_{i-(k-1)r}-a_{i-(k-2)r},
$$

(A.15)

$$
4\leqslant b_{i-(k-2)r}=5+a_{i-(k-2)r}-a_{i-kr}-a_{i-(k-1)r}.
$$

(A.16)

Adding up (A.15) and (A.16), we get

(A.17)

$$
10+a_{i-(k-3)r}-2a_{i-(k-1)r}-a_{i-kr}\geqslant8.
$$

Noting that *a*<sub>i</sub><sub>−</sub><sub>(k</sub><sub>−1</sub>

*)r= a*<sub>i</sub><sub>−</sub>*kr=* 1, we obtain from (A.17) and (A.16) that

$$
a_{i-(k-1)r}=a_{i-kr}=1
$$

(A.18)

$$
a_{i-(k-3)r}\geqslant1,\quad a_{i-(k-2)r}\geqslant1,
$$

which implies that

$$
a_{i-(k-3)r}+a_{i-(k-2)r}\geqslant2,
$$

contradicting with

*a*<sub>i</sub><sub>−</sub><sub>(k</sub>−3)r+ *a*<sub>i</sub><sub>−</sub><sub>(k</sub><sub>−2</sub>*)r1* in (A.9). Therefore

$$
a_{i-(k-3)r}+a_{i-(k-2)r}\leq1
$$

$$
c_{i-kr-r}\leqslant2.
$$

$$
c_{i}=3,c_{i-r}=c_{i-2r}=\cdots=c_{i-kr}=c_{i-kr-r}=2
$$

Finally, assume that ci= 3, *c*<sub>i</sub>−r= *c*<sub>i</sub><sub>−</sub>2r=···=c<sub>i</sub><sub>−</sub>*kr= c*<sub>i</sub>−kr−r= 2. From the conditions,
we know that (A.9), (A.10), (A.15) and (A.16) still hold. Since

$$
s_{i-(k-1)r}=b_{i-(k-1)r}-3c_{i-(k-1)r}+c_{i-k r-r}\geqslant0,
$$

$$
c_{i-(k-1)r}=c_{i-kr-r}=2
$$

we have

$$
4\leqslant b_{i-(k-1)r}=5+a_{i-(k-1)r}-a_{i-(k+1)r}-a_{i-kr}.
$$

(A.19)

Adding up (A.15) and (A.16), (A.16) and (A.19), respectively, we get

$$
2a_{i-(k-1)r}+a_{i-kr}-a_{i-(k-3)r}\leq2,
$$

(A.20)

$$
2a_{i-kr}+a_{i-(k+1)r}-a_{i-(k-2)r}\leq2.
$$

(A.21)

Adding up (A.20) and (A.21), we get

$$
2a_{i-(k-1)r}+3a_{i-kr}\leqslant4+(a_{i-(k-3)r}+a_{i-(k-2)r})-a_{i-(k+1)r}.
$$

Since *a*<sub>i</sub><sub>−</sub><sub>(k</sub>−3)r+ *a*

<sub>i</sub><sub>−</sub><sub>(k</sub><sub>−2</sub>)r1, it follows that

$$
a_{i-(k-3)r}+a_{i-(k-2)r}\leq1
$$

$$
2a_{i-(k-1)r}+3a_{i-kr}\leqslant5-a_{i-(k+1)r}\leqslant5.
$$

(A.22)

Now we would like to show that
*ai−kr*> 1. Since *ai*

*a*<sub>i</sub>−(k−1
−(k−1)r

)r+ ai−kr1. Assume to the contrary that *a*<sub>i</sub><sub>−</sub><sub>(k</sub>−1)r+
1, by (A.22), we have

$$
a_{i-(k-1)r}+a_{i-kr}\leq1
$$

$$
a_{i-(k-1)r}+
a_{i-kr}>1
$$

$$
a_{i-(k-1)r}\leqslant1
$$

$$
a_{i-(k-1)r}=1,\quad a_{i-kr}=1.
$$

(A.23)

Combining (A.16) with (A.23), we get

---

$$
a_{i-(k-2)r}\geqslant1.
$$

So *ai−(k−2)r+ ai−(k−1)r
ai−(k−1)r+ ai−kr*

2, contradicting with *a*<sub>i</sub><sub>−</sub><sub>(k</sub>−2)r+ *a*<sub>i</sub><sub>−</sub><sub>(k</sub><sub>−1</sub>*)r1* in (A.10). Hence
*1,*

$$
a_{i-(k-2)r}+a_{i-(k-1)r}\geqslant2
$$

$$
a_{i-(k-2)r}+a_{i-(k-1)r}\leq1
$$

$$
a_{i-(k-1)r}+a_{i-kr}\leq1,
$$

which in turn implies

$$
a_{i-kr}\leqslant1.
$$

This completes the proof.

✷

**Corollary A.5.** *If c*<sub>i</sub>= 3
ci−tr= *2, then c*<sub>i</sub><sub>−</sub>*tr*<sub>−</sub>r

*, then* ci−r2. *Let t* 1 *be an integer. If* ci= *3, c*<sub>i</sub><sub>−</sub>*r= c*<sub>i</sub><sub>−2</sub>r=···=
*2.*

$$
c_{i}=3_{i}
$$

$$
c_{i-r}\leqslant2.
$$

$$
t\geqslant1
$$

$$
l f c_{i}=3,c_{i-r}=c_{i-2r}=\cdots=
c_{i-tr}=2
$$

$$
c_{i-tr-r}\leqslant2
$$

**Proof.** The first assertion follows directly from Lemma A.2. For the second assertion, when
*t* = 1 (respectively, *t* = 2), the corollary follows from Lemma A.2 (respectively, Lemma A.3).
When *t* 3, the corollary follows directly from Theorem A.4. ✷

$$
t=1
$$

$$
t\geqslant3
$$

**Corollary A.6.** *Let t be an integer satisfying* 1 *t*
*2, ...,ci−(t−1)r2, then there exists,1 t* − 1

*m. Ifci= ci−tr
, such that* ci−r

= 3 *and c*<sub>i</sub><sub>−</sub><sub>r</sub>*2, c*<sub>i</sub><sub>−2</sub><sub>r</sub>
< *2.*

$$
1\leqslant t\leqslant m
$$

$$
c_{i}=c_{i-tr}=3
$$

$$
c_{i-r}\leqslant2,\;c_{i-2r}\leqslant
$$

$$
2,\ldots,c_{i-(t-1)r}\leqslant2
$$

$$
\ell,1\leqslant\ell\leqslant t-1
$$

$$
c_{i-\ell r}<2
$$

**Proof.** Using Corollary A.5, we see that the condition
to the contrary that for every ∈ {*1,2,...,t−* 1}, we have

ci= *ci−tr=* 3 implies that *t*
*i−r=* 2. That is, = 1. Assume
*c*

$$
t\neq1
$$

$$
c_{i}=c_{i-tr}=3
$$

$$
\ell\in\{1,2,\ldots,t-1\}
$$

$$
c_{i-\ell r}=2
$$

$$
c_{i}=3,\qquad c_{i-r}=c_{i-2r}=\cdots=c_{i-(t-1)r}=2.
$$

Then by Corollary A.5, we have
This completes the proof.

ci−tr2, contradicting with our assumption that *ci−tr=* 3.
✷

$$
c_{i-tr}\leqslant2
$$

$$
c_{i-tr}=3
$$

**Proof of Theorem A.1.**

As stated before, it suffices to prove that

$$
\sum_{i=0}^{m-1}c_{i}\leqslant2m.
$$

(A.24)

If *c*<sub>i</sub>2, for all i,0 *i*
that there exists an h,0
the sequence *ch, ch−r,...,c
c*<sup>h</sup><sup>−</sup><sup>i</sup><sup>1</sup><sup>r</sup>= *c*<sup>h</sup><sup>−</sup><sup>i</sup><sup>2</sup><sup>r</sup>=···=c
each *j* ∈ {*0,1,...,m*
...,isis−1+ 2, and *m*
each segment as follows:

*m−* 1, then the inequality (A.24) of course holds. So we assume
*h m* − 1, such that *c*<sub>h</sub>= 3. Since *gcd(m, r)* = 1, we see that
h−(m−1)ris just a permutation of *c0, c*<sub>1</sub>*,...,c*<sub>m</sub>−1. We assume that
h−<sup>i</sup><sup>s</sup><sup>r</sup>= 3, where 0 = *i*<sub>1</sub>< *i*<sub>2</sub>< ···i<sub>s</sub>< *m, s* 1, and *c*<sup>h</sup><sup>−</sup><sup>jr</sup>2 for
− 1} \ {*i1, i2,...,is}.* By Corollary A.5, we have i2i1+ 2, i3i2+ 2,
*i*<sub>s</sub>+ 2. Using Corollary A.6, we can bound the sum of the entries in

$$
c_{i}\leqslant2.
$$

$$
i,0\leqslant i\leqslant m-1
$$

$$
h,0\leqslant h\leqslant m-1
$$

$$
c_{h}=3
$$

$$
c_{0},c_{1},\ldots,c_{m-1}
$$

$$
c_{h},c_{h-r},\ldots,c_{h-(m-1)r}
$$

$$
c_{h-i_1\bar{r}}=c_{h-i_2\bar{r}}=\cdots=c_{h-i_s\bar{r}}=3
$$

$$
0=i_{1}<i_{2}<\cdots i_{s}<m,s\geqslant1
$$

$$
c_{h-jr}\leqslant2
$$

$$
j\in\{0,1,\ldots,m-1\}\setminus\{i_1,i_2,\ldots,i_s\}
$$

$$
i_{2}\geqslant i_{1}+2,i_{3}\geqslant i_{2}+2
$$

$$
\ldots,i_s\geqslant i_{s-1}+2
$$

$$
\begin{aligned}&c_{h-i_{1}r}+c_{h-(i_{1}+1)r}+\cdots+c_{h-(i_{2}-1)r}\leqslant2(i_{2}-i_{1}),\\&c_{h-i_{2}r}+c_{h-(i_{2}+1)r}+\cdots+c_{h-(i_{3}-1)r}\leqslant2(i_{3}-i_{2}),\\&\quad\vdots\\&c_{h-i_{s}r}+c_{h-(i_{s}+1)r}+\cdots+c_{h-(m-1)r}\leqslant2(m-i_{s}).\\ \end{aligned}
$$

Summing up the above inequalities, we obtain (A.24). The proof of the theorem is complete. ✷

---

### References

[1] S. Ball, M. Zieve, Symplectic spreads and permutation polynomials, in: Finite Fields and Applications, in: Lecture
Notes in Comput. Sci., vol. 2948, Springer, Berlin, 2004, pp. 79–88.
[2] L.D. Baumert, Cyclic Difference Sets, Lecture Notes in Math., vol. 182, Springer, 1971.
[3] B.C. Berndt, R.J. Evans, K.S. Williams, Gauss and Jacobi Sums, Wiley–Interscience, 1998.
[4] T. Beth, D. Jungnickel, H. Lenz, Design Theory, vol. I, second ed., Encyclopedia Math. Appl., vol. 78, Cambridge
Univ. Press, Cambridge, 1999.
[5] P. Camion, H.B. Mann, Antisymmetric difference sets, J. Number Theory 4 (1972) 266–268.
[6] J. Cannon, C. Playoust, An Introduction to MAGMA, University of Sydney, Sydney, Australia, 1993.
[7] Y.Q. Chen, Q. Xiang, S. Sehgal, An exponent bound on skew Hadamard abelian difference sets, Des. Codes Cryptogr. 4 (1994) 313–317.
[8] C. Ding, J. Yuan, A family of skew Hadamard difference sets, J. Combin. Theory Ser. A 113 (7) (2006) 1526–1535.
[9] J.W.P. Hirschfeld, Finite Projective Spaces of Three Dimensions, Oxford Math. Monogr., Oxford Sci. Publ., Clarendon Press, Oxford Univ. Press, New York, 1985.
[10] H. Hollmann, Q. Xiang, A proof of the Welch and Niho conjectures on cross-correlations of binary *m*-sequences,
Finite Fields Appl. 7 (2001) 253–286.
[11] E.C. Johnsen, Skew-Hadamard Abelian group difference sets, J. Algebra 4 (1966) 388–402.
[12] D. Jungnickel, On *λ*-ovals and difference sets, in: Contemporary Methods in Graph Theory, Bibliographisches Inst.,
Mannheim, 1990, pp. 429–448.
[13] D. Jungnickel, Difference sets, in: J. Dinitz, D.R. Stinson (Eds.), Contemporary Design Theory, A Collection of
Surveys, in: Wiley–Intersci. Ser. Discrete Math. Optim., Wiley, New York, 1992, pp. 241–324.
[14] W.M. Kantor, Ovoids and translation planes, Canad. J. Math. 34 (1982) 1195–1207.
[15] E.S. Lander, Symmetric Designs: An Algebraic Approach, London Math. Soc. Lecture Note Ser., vol. 74, Cambridge Univ. Press, 1983.
[16] S. Lang, Cyclotomic Fields, Springer, New York, 1978.
[17] R. Lidl, H. Niederreiter, Finite Fields, second ed., Encyclopedia Math. Appl., vol. 20, Cambridge Univ. Press,
Cambridge, 1997.
[18] T.S. Michael, W.D. Wallis, Skew-Hadamard matrices and the Smith normal form, Des. Codes Cryptogr. 13 (1998)
173–176.
[19] R.G. Stanton, D.A. Sprott, A family of difference sets, Canad. J. Math. 10 (1958) 73–77.
[20] Q. Xiang, Recent progress in algebraic design theory, Finite Fields Appl. 11 (2005) 622–653.