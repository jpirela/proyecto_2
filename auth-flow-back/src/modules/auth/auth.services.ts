//const email_sender = require('./../utils/email');
import * as auth from './auth.model';
import bcrypt from 'bcryptjs';
import jwt from 'jsonwebtoken';
import { LoginData, UserData } from './auth.interfaces';


// Register a new user
export const registerUser = async (data: UserData) => {
  const { name, email, password, picture } = data;

  console.log("DATA ===>", data);

  // Validate input data
  if (!name || name.trim() === "") {
    throw {
      success: false,
      code: 400,
      message: "EMPTY_NAME",
    };
  } else if (!email || email.trim() === "") {
    throw {
      success: false,
      code: 400,
      message: "EMPTY_EMAIL",
    };
  } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
    throw {
      success: false,
      code: 400,
      message: "INVALID_EMAIL",
    };
  } else if (!password || password === "") {
    throw {
      success: false,
      code: 400,
      message: "EMPTY_PASSWORD",
    };
  }
  }

  // Hash the password
  const hashedPassword = bcrypt.hashSync(password|| 10);

  // Create a new user
  const newUser = await auth.createUser({
    name,
    email,
    password: hashedPassword,
    picture: picture ?? undefined
  });

  if (newUser) {
    return {
      success: true,
      code: 201,
      data: "User registered successfully",
    };
  } else {
    throw {
      success: false,
      code: 500,
      message: "SYSTEM_ERROR",
    };
  }
};
