INSERT INTO regions (region_name) VALUES
(
 'Arecibo'
);
INSERT INTO regions (region_name) VALUES
(
 'Bayamón'
);
INSERT INTO regions (region_name) VALUES
(
 'Carolina'
);
INSERT INTO regions (region_name) VALUES
(
 'Caguas'
);
INSERT INTO regions (region_name) VALUES
(
 'Mayagüez'
);
INSERT INTO regions (region_name) VALUES
(
 'Ponce'
);
INSERT INTO regions (region_name) VALUES
(
 'San Juan'
);
INSERT INTO regions (region_name) VALUES
(
 'All Regions'
);
INSERT INTO data_sources (source_name, source_url) VALUES
(
 'poweroutage.us',
 'https://poweroutage.us/area/county/'
);
INSERT INTO data_sources (source_name, source_url) VALUES
(
 'Luma Portal',
 'https://miluma.lumapr.com/outages/clientsWithoutService'
);

INSERT INTO source_region_mappings (source_id, region_id, source_specific_region_id) VALUES
(
 1, -- poweroutage.us
 1, -- Arecibo
 '5468'
);
INSERT INTO source_region_mappings (source_id, region_id, source_specific_region_id) VALUES
(
 1, -- poweroutage.us
 2, -- Bayamón
 '5469'
);
INSERT INTO source_region_mappings (source_id, region_id, source_specific_region_id) VALUES
(
 1, -- poweroutage.us
 3, -- Carolina
 '5471'
);
INSERT INTO source_region_mappings (source_id, region_id, source_specific_region_id) VALUES
(
 1, -- poweroutage.us
 4, -- Caguas
 '5470'
);
INSERT INTO source_region_mappings (source_id, region_id, source_specific_region_id) VALUES
(
 1, -- poweroutage.us
 5, -- Mayaguez
 '5472'
);
INSERT INTO source_region_mappings (source_id, region_id, source_specific_region_id) VALUES
(
 1, -- poweroutage.us
 6, -- Ponce
 '5473'
);
INSERT INTO source_region_mappings (source_id, region_id, source_specific_region_id) VALUES
(
 1, -- poweroutage.us
 7, -- San Juan
 '5474'
);