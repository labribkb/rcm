import rcm

conf_a = rcm.random_conf_mat()
conf_b = rcm.random_conf_mat()

print("A=", conf_a, "B=", conf_b)

r = rcm.build_rcm(conf_a, conf_b)
fname = r.show(with_sliders=False)

print(f"Think to delete {fname}")