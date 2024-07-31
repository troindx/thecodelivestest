print("Loaded init-mongo.js");
db = db.getSiblingDB('admin');  // switch to the admin database
db.auth(process.env.MONGO_INITDB_ROOT_USERNAME, process.env.MONGO_INITDB_ROOT_PASSWORD);  // authenticate as root

const username = process.env.MONGODB_USER;
const password = process.env.MONGODB_PASSWORD;
const dbName = process.env.MONGO_INIT_DATABASE_NAME;
const testDbName = process.env.MONGODB_TEST_DATABASE_NAME;

try {
    db = db.getSiblingDB(dbName);  // switch to your target database

    db.createUser({
        user: username,
        pwd: password,
        roles: [
            {
                role: "readWrite",
                db: dbName
            },
            {
                role: "readWrite",
                db: testDbName
            }
        ]
    });

    print(`User ${username} created successfully in databases ${dbName} and ${testDbName}`);
} catch (e) {
    print(`Error creating user ${username}: ${e}`);
}
