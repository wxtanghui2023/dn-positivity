# RESULT-2026-09-30-DS243i — (乙) 第一刀：交叉谱消元得**独立新条件** ✓✓ —— 循环交叉谱 $=0$ ⟹ $|\hat f|^2=61$ ⟹ **群环 $f\tilde f=180G+61\delta$** ⟹ **$T=\sum_{i<j}|R_i\cap R_j|=60$**

> 空间 B｜非 C 号｜唐先生 13:26「开 (乙)；先写成可消元的群环形式；目标不是 SAT 而是找非平凡乘积谱恒等式」｜**不主张任何新值**（V290）
> 时间：2026-09-30 14:2x

**已查地图**：承 `DS243h`（(甲) 恒等式闭合 ⟹ 计数层饱和）
D0: 本档对象 = **(b) 之 Fourier 消元**（新数学对象：**乘积谱层** ✓ 非计数层）
D1: 0（产出 = **一条消元恒等式 ＋ 一条独立新条件 ＋ 一条一致性核验** ⚠️✓）

---

## §0 记法与 (b) 的正确形式（本档已核 ✓）

$$C_{ij}(w):=\#\{x\in R_i:\ x-w\in R_j\}\ (i,j\in\{0,1,2\});\quad \text{Fourier}:\ \hat C_{ij}(\chi)=\hat f_i(\chi)\overline{\hat f_j(\chi)}\ ✓$$
$$\textbf{(a)}:\ \forall\,0\ne w\in H:\ \sum_i C_{ii}(w)=60\ \Longleftrightarrow\ \sum_i|\hat f_i(\chi)|^2=61\ (\chi\ne1)\ ✓$$
$$\textbf{(b)}:\ \forall w\in H:\ C_{10}(w)+C_{21}(w)+C_{02}(w)=60\ \ \Longleftrightarrow\ \forall\chi\ne1:\ \hat f_1\overline{\hat f_0}+\hat f_2\overline{\hat f_1}+\hat f_0\overline{\hat f_2}=0$$
$$\qquad(\textbf{循环交叉谱为零} ✓✓\ \text{—— 这正是唐先生预告之“乘积谱”层} ✓)$$

## §1 **结论链（本档核心 ✓）**

$$\text{恒等式（500 随机复数核验 ✓）}:\ |z_0+z_1+z_2|^2=\sum_i|z_i|^2+2\mathrm{Re}\big(\overline{z_0}z_1+\overline{z_1}z_2+\overline{z_2}z_0\big)$$
$$\text{循环三对} = \text{全部三对} \Longrightarrow \sum_{i\ne j}\hat f_i\overline{\hat f_j}=2\mathrm{Re}(\text{循环和})=0\ \ (\text{由 (b)})$$
$$\therefore\ \boxed{\big|\hat f(\chi)\big|^2=61\quad(\chi\ne1),\qquad f:=f_0+f_1+f_2}\quad(\textbf{总量函数之谱} ✓✓\ \text{与 (a) 的“一阶能量和”不同层})$$
$$\Longrightarrow\ \textbf{群环恒等式}:\quad \boxed{f\tilde f=180\,G+61\,\delta}\quad(G=\textstyle\sum_{h\in H}h)$$
$$\qquad\text{即 }(f\star f)(z)=180\ (z\ne0);\quad (f\star f)(0)=\sum_x f(x)^2=241$$

## §2 **独立新条件：$T=60$**（本档核心成果 ✓✓）

$$\sum_x f(x)^2=121+2T,\qquad T:=\sum_{i<j}|R_i\cap R_j| \Longrightarrow 121+2T=241 \Longrightarrow \boxed{T=60}$$
$$\therefore\ \textbf{三 fiber 之总两两交} = 60\ (\text{例: }20+20+20)\ \text{—— \textbf{不被计数层蕴含}} ✓\ (\text{≠ (甲) 之推论})$$

## §3 **一致性核验（强 ✓）**

$$\text{全部差分记账}:\ \underbrace{4921}_{H\ \text{部分}} + \underbrace{162\times60}_{9720} = 14641 = 121^2\ ✓✓\ (\text{逐字吻合})$$
$$\qquad(H\ \text{部分}: c(0)=121,\ c(z\ne0)=60\ \text{共 80 个} = 4800;\ \text{非零陪集 } 243-81=162\ \text{个} \times 60\ ✓)$$
$$\text{四阶矩自洽}:\ \sum_z c_z^2 = 241^2+80\cdot180^2 = 2650081 = \tfrac1{81}\big(121^4+80\cdot61^2\big)\ ✓✓$$

## §4 f-层可行性探针（**仅探针，不作结论** ⚠️）

$$\text{目标}:\ f\in\{0,1,2,3\}^{81},\ \sum f=121,\ (f\star f)(z)=180\ (z\ne0)$$
$$\text{探针（3 restarts × 3000 步）}: \text{最优偏差} = 158\ (\ne0) \Longrightarrow \textbf{未找到}; \ \textbf{但探针零 infeasibility 证据} ✗\ (\text{遵纪律: }\ne\text{不存在})$$
$$\textbf{附带判据（严格）}:\ \text{“}f\in\{1,3\}\ \text{两值”ansatz 不可能 ⟹ |T\cap(T+z)|=19/4\notin\mathbb Z\ ✗\ \text{（一个 ansatz 被排除，非一般矛盾）}$$

## §5 判读与去向

$$\boxed{\text{(乙) \textbf{首次产生独立条件} ⟹ 计数层之外\ \textbf{确有未饱和结构} ✓✓}}\quad(\text{与 (甲)/(a) 之饱和形成对比})$$
$$\textbf{下一刀（最干净之新靶）}:\ f\text{-层可行性 —— }81\ \text{变量、值域 }\{0,\dots,3\}、\sum f=121、80\ \text{个自相关等式}$$
$$\qquad\text{若\ \textbf{不可行} ⟹ \textbf{真正的 P1}（且直接给出\ \textbf{非存在性}}：因 }f\text{-条件为\textbf{必要} ✓✓)$$
$$\qquad\text{若可行 ⟹ 继续加 fiber 分解 }f=f_0+f_1+f_2\ (f_i\in\{0,1\})\ \text{与 (a) 联立} ✓$$
$$\textbf{注意（照令保持）}:\ \text{61-乘子假设\ \textbf{仍待核} ⚠️;\ 本档结论\ \textbf{不依赖}它（(b) 为原始差集条件之直接推论 ✓）}$$

## §7 【技术词回查】（`scripts/tech_word_check.sh` 逐字输出 ✓）

```
技术词 交叉谱        命中文件数=1    :: ./RESULT-2026-09-30-DS243i-...-T60.md
技术词 乘积谱        命中文件数=1    :: ./RESULT-2026-09-30-DS243i-...-T60.md
技术词 群环恒等式  命中文件数=2    :: ./RESULT-2026-09-30-DS243i-...-T60.md ./RESULT-2026-09-30-DS243g-two-layer-Fourier-compression-order9-kernels-all-feasible.md
技术词 总量函数     命中文件数=1    :: ./RESULT-2026-09-30-DS243i-...-T60.md
```

$$	extbf{分类}:\ 	ext{交叉谱／乘积谱／总量函数} = 	extbf{本档新增} ✓\ (	ext{其余命中仅本档自身});\quad 	ext{群环恒等式} = 	extbf{档案已有（本线，前瞻 }DS243g	ext{）} ✓\ 	ext{引用不计}$$
$$	ext{空间 A/B 分离（AMEND-27）}:\ 	ext{上述命中\ 	extbf{全在本线（空间 B）}};\ 	ext{无跨空间同名} ✓$$
$$	ext{通用词（不计）}:\ 	ext{“交叉”／“总量”／“群环”作裸词不计 ✓}$$


## §6 边界与纪律

$$\textbf{(D1)}\ \text{无 P1（探针不作证据）} ⚠️;\quad \textbf{(D2)}\ \text{skew 已移出主链} ✓;\quad \textbf{(D3)}\ \text{未主张任何新值／未取文献原文／未碰 RH} ✓$$

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=NA R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
