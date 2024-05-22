# Medical Shop Management System

This project implements APIs for a Medical Shop Management System using Flask and SQLite3. It provides APIs for creating users, managing products, and performing user-related operations like blocking, approving, and updating user levels.

## Features

- **User Management**:
  - Create new users with details such as name, password, address, email, phone, and pincode.
  - Get all users or retrieve a specific user by ID.
  - Block, approve, or update the level of a user.

- **Product Management**:
  - Add new products with details like name, brand, description, price, category, stock, and active status.
  - Update product status, price, or stock.

## Usage

- **Create User**:
  - Endpoint: `/CreateUser`
  - Method: POST
  - Parameters: name, password, address, email, phone, pincode

- **Get All Users**:
  - Endpoint: `/getAllUsers`
  - Method: GET

- **Get Specific User**:
  - Endpoint: `/getSpecificUsers`
  - Method: GET
  - Parameters: user_id

- **Block User**:
  - Endpoint: `/userBlocked`
  - Method: PATCH
  - Parameters: id, blocked

- **Approve User**:
  - Endpoint: `/userApproved`
  - Method: PATCH
  - Parameters: id, approved

- **Update User Level**:
  - Endpoint: `/userLevel`
  - Method: PATCH
  - Parameters: id, level

- **Create Product**:
  - Endpoint: `/createProduct`
  - Method: POST
  - Parameters: name, brand, description, price, category, stock, isActive

- **Update Product Status**:
  - Endpoint: `/productisActive`
  - Method: PATCH
  - Parameters: name, isActive

- **Update Product Price**:
  - Endpoint: `/updatePrice`
  - Method: PATCH
  - Parameters: name, price

- **Update Product Stock**:
  - Endpoint: `/updateStock`
  - Method: PATCH
  - Parameters: name, stock

## Database Schema

The application uses SQLite3 with the following tables:

- **User**:
  - id
  - user_id
  - password
  - level
  - date_of_creation
  - approved
  - blocked
  - name
  - address
  - email
  - phone
  - pincode

- **Products**:
  - product_id
  - name
  - brand
  - description
  - price
  - category
  - stock
  - isActive

## Developer

- **Name:** ANIMESH NILAWAR
- **GitHub:** https://github.com/AnimeshNilawar


## 🔗 Links

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/animesh-nilawar/)

[![linkedin](https://img.shields.io/badge/instagram-bc2a8d?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/aniiimesh1/)

## Contributing

We welcome contributions from the community to enhance our APIs further. Feel free to fork the repository, make improvements, and submit pull requests.

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/awesome-feature`
3. Make changes and commit: `git commit -m 'Add awesome feature'`
4. Push to the branch: `git push origin feature/awesome-feature`
5. Open a pull request.



## License

This is licensed under the [MIT License](https://choosealicense.com/licenses/mit/), allowing for open collaboration and innovation in the spirit of shared knowledge.

Thank you for being part of this API! If you have any questions or suggestions, feel free to open an issue or reach out to us. Happy coding! 🚀📞
