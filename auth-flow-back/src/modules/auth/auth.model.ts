export const createUser = async (data: UserData) => {
  let pool;
  try {
    pool = await getDbConnection();
    const result = await pool.request()
      .input('name', sql.NVarChar, data.name)
      .input('email', sql.NVarChar, data.email)
      .input('password', sql.NVarChar, data.password)
      .input('stateID', sql.Int, data.stateID)
      .input('cityID', sql.Int, data.cityID)
      .input('picture', sql.NText, data.picture ?? null)
      .query(`
        INSERT INTO users (Fullname, Email, Password,Picture)
        OUTPUT INSERTED.UserID
        VALUES (@name, @email, @password, @picture)
      `);

    return result.recordset[0]?.UserID || null;
  } catch (err) {
    if (err instanceof sql.RequestError && err.number === 2627) {
      throw new Error('El email ya está registrado');
    }
    console.error('Error en createUser:', err);
    throw err;
  } finally {
    if (pool) await pool.close();
  }
}

// Get user by email to validate (versión mejorada)
export const validateUserEmail = async (email: string) => {
  let pool;
  try {
    pool = await getDbConnection();
    const result = await pool.request()
      .input('email', sql.VarChar, email)
      .query(`
        SELECT 
          UserID AS id, 
          Fullname AS name, 
          Email AS email,
          IsActivated AS active, 
          IsDeleted AS deleted
        FROM users
        WHERE Email = @email
        AND IsActivated = 1
        AND IsDeleted = 0
      `);

    return result.recordset[0] || null;
  } catch (err) {
    console.error('Error en validateUserEmail:', err);
    throw err;
  } finally {
    if (pool) await pool.close();
  }
}

// Get user data for login (versión mejorada)
export const getLoginData = async (email: string) => {
  let pool;
  try {
    pool = await getDbConnection();
    const result = await pool.request()
      .input('email', sql.VarChar, email)
      .query(`
        SELECT
          UserID AS id,
          Fullname AS name,
          Email AS email,
          Password AS password,
          IsActivated AS active,
          IsDeleted AS deleted,
          StateID AS stateId,
          CityID AS cityId,
          Picture AS picture
        FROM users
        WHERE Email = @email
        AND IsActivated = 1
        AND IsDeleted = 0
      `);

    return result.recordset[0] || null;
  } catch (err) {
    console.error('Error en getLoginData:', err);
    throw err;
  } finally {
    if (pool) await pool.close();
  }
}
