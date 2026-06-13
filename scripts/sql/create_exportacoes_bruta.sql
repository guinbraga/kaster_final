CREATE TABLE if not exists exportacoes_bruta (
	id serial PRIMARY KEY,
	co_ano varchar(4),
	co_mes varchar(2),
	co_ncm varchar(10),
	co_unid varchar(3),
	co_pais varchar(4),
	sg_uf_ncm varchar(3),
	co_via varchar(2),
	co_urf varchar(8),
	qt_estat bigint,
	kg_liquido bigint,
	vl_fob bigint
)
