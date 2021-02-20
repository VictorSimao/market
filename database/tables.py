table_salesman = '''
        CREATE TABLE if not exists salesman (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fantasy_name TEXT NOT NULL,
            company_name TEXT NOT NULL,
            cnpj TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            address TEXT NOT NULL
            );
        '''

table_product = '''
        CREATE TABLE if not exists product (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            value TEXT NOT NULL
            );
        '''
table_product_category = '''
        CREATE TABLE if not exists product_category (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER NOT NULL,
            category_id INTEGER NOT NULL,
            FOREIGN KEY (product_id) REFERENCES product (id),
            FOREIGN KEY (category_id) REFERENCES category (id)
            );
        '''
    
table_category = '''
        CREATE TABLE if not exists category (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL
            );
        '''

table_marketplace = '''
        CREATE TABLE if not exists marketplace (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            site TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT NOT NULL,
            technician_contact TEXT NOT NULL,
            );
        '''
