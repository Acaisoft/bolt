INSERT INTO configuration_type (name, description, slug_name) VALUES
    ('Performance', 'Select this type if your repository contains performance tests', 'load_tests');


INSERT INTO parameter (name, param_name, param_type, slug_name, default_value, tooltip) VALUES
    ('duration (s)', '-t', 'str', 'load_tests_duration', '10', 'How long your test will run.'),
    ('users/second', '-r', 'int', 'load_tests_rampup', '500', 'How many users will be spawned every second until the target amount is reached.'),
    ('users', '-u', 'int', 'load_tests_users', '1000', 'Total amount of users to be spawned.'),
    ('monitoring duration', '-md', 'int', 'monitoring_duration', '10'),
    ('monitoring interval', '-mi', 'int', 'monitoring_interval', '5'),
    ('host', '-H', 'str', 'load_tests_host', '', 'Address of service to be tested.');
