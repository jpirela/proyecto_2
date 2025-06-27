package com.todolist.Manudev01.urbe.User.Services;

import com.todolist.Manudev01.urbe.Database.DatabaseConnection;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class userServices {

    public String userRegister(String nombre, String apellido, String usuario, String contrasena) {
        String sql = "INSERT INTO usuarios(nombre, apellido, usuario, contrasena) VALUES (?, ?, ?, ?)";
        try (Connection connection = DatabaseConnection.getConnection();
             PreparedStatement preparedStatement = connection.prepareStatement(sql)) {
            preparedStatement.setString(1, nombre);
            preparedStatement.setString(2, apellido);
            preparedStatement.setString(3, usuario);
            preparedStatement.setString(4, contrasena);
            int rowsAffected = preparedStatement.executeUpdate();
            if (rowsAffected > 0) {
                return "User registered successfully!";
            } else {
                return "Failed to register user.";
            }
        } catch (SQLException e) {
            return "Error during user registration: " + e.getMessage();
        }
    }

    public String getUserById(int userId) {
        String sql = "SELECT * FROM usuarios WHERE id = ?";
        try (Connection connection = DatabaseConnection.getConnection();
             PreparedStatement preparedStatement = connection.prepareStatement(sql)) {
            preparedStatement.setInt(1, userId);
            var resultSet = preparedStatement.executeQuery();
            if (resultSet.next()) {
                return "User found: " + resultSet.getString("usuario");
            } else {
                return "User not found.";
            }
        } catch (SQLException e) {
            return "Error retrieving user: " + e.getMessage();
        }
    }
}