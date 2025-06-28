# ============================================================================
# FRONTEND - INTERFAZ DE USUARIO Y TEMPLATES
# ============================================================================

class VentasFrontend:
    """Clase para manejar la interfaz de usuario y estilos"""
    
    @staticmethod
    def obtener_html_template():
        """Retorna el template HTML completo con estilos y JavaScript"""
        return """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registro de Ventas</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            overflow: hidden;
        }

        .header {
            background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }

        .header h1 {
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 10px;
        }

        .header p {
            font-size: 1.1rem;
            opacity: 0.9;
        }

        .content {
            padding: 40px;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 40px;
        }

        .form-section {
            background: #f8fafc;
            padding: 30px;
            border-radius: 15px;
            border: 1px solid #e2e8f0;
        }

        .form-section h2 {
            color: #1e293b;
            font-size: 1.5rem;
            margin-bottom: 25px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .form-group {
            margin-bottom: 20px;
        }

        .form-group label {
            display: block;
            margin-bottom: 8px;
            color: #374151;
            font-weight: 500;
            font-size: 0.9rem;
        }

        .form-group input {
            width: 100%;
            padding: 12px 16px;
            border: 2px solid #e5e7eb;
            border-radius: 10px;
            font-size: 1rem;
            transition: all 0.3s ease;
            background: white;
        }

        .form-group input:focus {
            outline: none;
            border-color: #4f46e5;
            box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1);
        }

        .btn {
            background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
            color: white;
            border: none;
            padding: 14px 28px;
            border-radius: 10px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            width: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        }

        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(79, 70, 229, 0.3);
        }

        .btn:active {
            transform: translateY(0);
        }

        .btn-danger {
            background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
        }

        .btn-danger:hover {
            box-shadow: 0 10px 20px rgba(239, 68, 68, 0.3);
        }

        .btn-warning {
            background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        }

        .btn-warning:hover {
            box-shadow: 0 10px 20px rgba(245, 158, 11, 0.3);
        }

        .ventas-section {
            background: white;
            border-radius: 15px;
            border: 1px solid #e2e8f0;
        }

        .ventas-section h2 {
            color: #1e293b;
            font-size: 1.5rem;
            margin-bottom: 25px;
            padding: 30px 30px 0 30px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .ventas-list {
            padding: 0 30px 30px 30px;
            max-height: 400px;
            overflow-y: auto;
        }

        .venta-item {
            background: #f8fafc;
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 15px;
            border-left: 4px solid #4f46e5;
            transition: all 0.3s ease;
        }

        .venta-item:hover {
            transform: translateX(5px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }

        .venta-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
        }

        .producto-nombre {
            font-weight: 600;
            color: #1e293b;
            font-size: 1.1rem;
        }

        .venta-details {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            font-size: 0.9rem;
            color: #6b7280;
        }

        .total-venta {
            background: linear-gradient(135deg, #10b981 0%, #059669 100%);
            color: white;
            padding: 8px 12px;
            border-radius: 8px;
            font-weight: 600;
            font-size: 0.9rem;
        }

        .venta-actions {
            margin-top: 10px;
            display: flex;
            gap: 10px;
        }

        .btn-small {
            padding: 6px 12px;
            font-size: 0.8rem;
            width: auto;
        }

        .empty-state {
            text-align: center;
            padding: 40px;
            color: #6b7280;
        }

        .empty-state i {
            font-size: 3rem;
            margin-bottom: 15px;
            opacity: 0.5;
        }

        .stats {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            margin-bottom: 30px;
            padding: 0 30px;
        }

        .stat-card {
            background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
            padding: 20px;
            border-radius: 12px;
            text-align: center;
            border: 1px solid #e2e8f0;
        }

        .stat-number {
            font-size: 2rem;
            font-weight: 700;
            color: #4f46e5;
            margin-bottom: 5px;
        }

        .stat-label {
            font-size: 0.9rem;
            color: #6b7280;
            font-weight: 500;
        }

        .actions-bar {
            padding: 0 30px 20px 30px;
            display: flex;
            gap: 10px;
            justify-content: flex-end;
        }

        @media (max-width: 768px) {
            .content {
                grid-template-columns: 1fr;
                gap: 20px;
            }
            
            .stats {
                grid-template-columns: 1fr;
            }
            
            .header h1 {
                font-size: 2rem;
            }
            
            .actions-bar {
                flex-direction: column;
            }
        }

        .success-message {
            background: #10b981;
            color: white;
            padding: 12px 20px;
            border-radius: 8px;
            margin-bottom: 20px;
            display: none;
            animation: slideIn 0.3s ease;
        }

        .error-message {
            background: #ef4444;
            color: white;
            padding: 12px 20px;
            border-radius: 8px;
            margin-bottom: 20px;
            display: none;
            animation: slideIn 0.3s ease;
        }

        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(-10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1><i class="fas fa-chart-line"></i> Registro de Ventas</h1>
            <p>Sistema de gestión y control de ventas</p>
        </div>
        
        <div class="content">
            <div class="form-section">
                <h2><i class="fas fa-plus-circle"></i> Nueva Venta</h2>
                <div id="successMessage" class="success-message">
                    <i class="fas fa-check"></i> Venta registrada exitosamente
                </div>
                <div id="errorMessage" class="error-message">
                    <i class="fas fa-exclamation-triangle"></i> <span id="errorText"></span>
                </div>
                <form id="ventaForm">
                    <div class="form-group">
                        <label for="producto"><i class="fas fa-box"></i> Producto</label>
                        <input type="text" id="producto" name="producto" required placeholder="Nombre del producto">
                    </div>
                    <div class="form-group">
                        <label for="cantidad"><i class="fas fa-hashtag"></i> Cantidad</label>
                        <input type="number" id="cantidad" name="cantidad" required placeholder="Cantidad vendida" min="1">
                    </div>
                    <div class="form-group">
                        <label for="precio"><i class="fas fa-dollar-sign"></i> Precio Unitario</label>
                        <input type="number" id="precio" name="precio" step="0.01" required placeholder="Precio por unidad" min="0.01">
                    </div>
                    <button type="submit" class="btn">
                        <i class="fas fa-save"></i> Registrar Venta
                    </button>
                </form>
            </div>
            
            <div class="ventas-section">
                <h2><i class="fas fa-list"></i> Ventas Registradas</h2>
                <div class="stats">
                    <div class="stat-card">
                        <div class="stat-number" id="totalVentas">0</div>
                        <div class="stat-label">Total Ventas</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number" id="totalProductos">0</div>
                        <div class="stat-label">Productos Vendidos</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number" id="totalIngresos">$0</div>
                        <div class="stat-label">Ingresos Totales</div>
                    </div>
                </div>
                <div class="actions-bar">
                    <button class="btn btn-warning btn-small" onclick="ventasUI.limpiarTodasLasVentas()">
                        <i class="fas fa-trash-alt"></i> Limpiar Todo
                    </button>
                </div>
                <div class="ventas-list" id="ventasList">
                    <div class="empty-state">
                        <i class="fas fa-inbox"></i>
                        <p>No hay ventas registradas</p>
                        <p>Comienza agregando tu primera venta</p>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        class VentasUI {
            constructor() {
                this.init();
            }

            init() {
                this.bindEvents();
                this.cargarVentas();
            }

            bindEvents() {
                document.getElementById('ventaForm').addEventListener('submit', (e) => {
                    e.preventDefault();
                    this.registrarVenta(e.target);
                });
            }

            mostrarMensaje(tipo, texto) {
                const successMsg = document.getElementById('successMessage');
                const errorMsg = document.getElementById('errorMessage');
                const errorText = document.getElementById('errorText');

                if (tipo === 'success') {
                    successMsg.style.display = 'block';
                    errorMsg.style.display = 'none';
                    setTimeout(() => {
                        successMsg.style.display = 'none';
                    }, 3000);
                } else {
                    errorText.textContent = texto;
                    errorMsg.style.display = 'block';
                    successMsg.style.display = 'none';
                    setTimeout(() => {
                        errorMsg.style.display = 'none';
                    }, 5000);
                }
            }

            actualizarEstadisticas(ventas) {
                const totalVentas = ventas.length;
                const totalProductos = ventas.reduce((sum, v) => sum + v.cantidad, 0);
                const ingresosTotales = ventas.reduce((sum, v) => sum + v.total, 0);
                
                document.getElementById('totalVentas').textContent = totalVentas;
                document.getElementById('totalProductos').textContent = totalProductos;
                document.getElementById('totalIngresos').textContent = '$' + ingresosTotales.toFixed(2);
            }

            async registrarVenta(form) {
                const formData = new FormData(form);
                
                try {
                    const response = await fetch('/ventas', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify({
                            producto: formData.get('producto'),
                            cantidad: formData.get('cantidad'),
                            precio: formData.get('precio')
                        })
                    });

                    const result = await response.json();
                    
                    if (result.status === 'success') {
                        form.reset();
                        this.cargarVentas();
                        this.mostrarMensaje('success');
                    } else {
                        this.mostrarMensaje('error', result.message);
                    }
                } catch (error) {
                    this.mostrarMensaje('error', 'Error de conexión');
                }
            }

            async eliminarVenta(ventaId) {
                if (!confirm('¿Estás seguro de que quieres eliminar esta venta?')) {
                    return;
                }

                try {
                    const response = await fetch(`/ventas/${ventaId}`, {
                        method: 'DELETE'
                    });

                    const result = await response.json();
                    
                    if (result.status === 'success') {
                        this.cargarVentas();
                        this.mostrarMensaje('success', 'Venta eliminada exitosamente');
                    } else {
                        this.mostrarMensaje('error', result.message);
                    }
                } catch (error) {
                    this.mostrarMensaje('error', 'Error al eliminar la venta');
                }
            }

            async limpiarTodasLasVentas() {
                if (!confirm('¿Estás seguro de que quieres eliminar TODAS las ventas? Esta acción no se puede deshacer.')) {
                    return;
                }

                try {
                    const response = await fetch('/ventas/limpiar', {
                        method: 'DELETE'
                    });

                    const result = await response.json();
                    
                    if (result.status === 'success') {
                        this.cargarVentas();
                        this.mostrarMensaje('success', 'Todas las ventas han sido eliminadas');
                    } else {
                        this.mostrarMensaje('error', result.message);
                    }
                } catch (error) {
                    this.mostrarMensaje('error', 'Error al limpiar las ventas');
                }
            }

            async cargarVentas() {
                try {
                    const response = await fetch('/ventas');
                    const data = await response.json();
                    
                    let lista = document.getElementById('ventasList');
                    
                    if (data.length === 0) {
                        lista.innerHTML = `
                            <div class="empty-state">
                                <i class="fas fa-inbox"></i>
                                <p>No hay ventas registradas</p>
                                <p>Comienza agregando tu primera venta</p>
                            </div>
                        `;
                    } else {
                        lista.innerHTML = '';
                        data.forEach(v => {
                            let li = document.createElement('div');
                            li.className = 'venta-item';
                            li.innerHTML = `
                                <div class="venta-header">
                                    <div class="producto-nombre">${v.producto}</div>
                                    <div class="total-venta">$${v.total.toFixed(2)}</div>
                                </div>
                                <div class="venta-details">
                                    <div><i class="fas fa-hashtag"></i> Cantidad: ${v.cantidad}</div>
                                    <div><i class="fas fa-dollar-sign"></i> Precio: $${v.precio.toFixed(2)}</div>
                                </div>
                                <div class="venta-actions">
                                    <button class="btn btn-danger btn-small" onclick="ventasUI.eliminarVenta(${v.id})">
                                        <i class="fas fa-trash"></i> Eliminar
                                    </button>
                                </div>
                            `;
                            lista.appendChild(li);
                        });
                    }
                    
                    this.actualizarEstadisticas(data);
                } catch (error) {
                    this.mostrarMensaje('error', 'Error al cargar las ventas');
                }
            }
        }

        // Inicializar la interfaz de usuario
        const ventasUI = new VentasUI();
    </script>
</body>
</html>
""" 