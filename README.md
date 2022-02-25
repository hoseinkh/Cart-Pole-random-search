# Control of Cart Pole with a Policy Search

Policy search algorithm for controling a Cart Pole.

<br />

Task

The goal is to design a control policy to keep a Cart Pole leveled



Solution

We assume a simple linear policy. We use a simple algorithm to find the optimal policy by brute-force **policy search**.

---



The general form of the cart-pole is shown in the following figure.



<p float="left">
  <img src="/figs/CartPole_model.png" width="450" />
</p>






The states are shown in this figure as well. So we have four features to describe each state. We **assume** that the policy is a **linear function** of the state features, and the goal is to find the optimal policy.

So the policy is as follows:

<p float="left">
  <img src="/figs/CartPole_policy_random_search.png" width="450" />
</p>


So the goal is to find the optimal weight $W$.

<br />

## A Random Policy

Now, we first run a simple random policy. Ofcourse we expect it fail immediately!

<p float="left">
  <img src="/figs/CartPole_a_random_policy.gif" width="450" />
</p>




We can see that this policy quickly fails.

## Optimal Policy

In order to find the optimal policy, we search through different random policies, and find the one that has the longest average life. In the following figure we can see the performance of different random policies that we have explored.



<p float="left">
  <img src="/figs/CartPole_avgtime_random_search.png" width="450" />
</p>




The winner of this policy is tested in the following figure:

<p float="left">
  <img src="/figs/CartPole_optimal_random_search.gif" width="450" />
</p>


<br />

