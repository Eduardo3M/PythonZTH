/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.mavenproject2;

/**
 *
 * @author UCV
 */

import javax.swing.JOptionPane;
       
public class EM_LAB_S3 {
        public static void main(String[] args) {
            System.out.println("Hola");
            Uno_ApruebaCurso();
            Dos_ParImpar();
            Tres_ValorAbsoluto();
            Cuatro_EcuacionSegundoGrado();
            Cinco_Calculadora();
            Seis_OfertaTienda();
            Siete_PositivaExpresion();
            Ocho_NegativaExpresion();
            Nueve_Temperatura();
            Diez_alumnos();
            Once_clasificacion();
            Doce_SumaProductoPares();
            Trece_TrianguloAngulos();
            Catorce_Dosnumeros();
            Quince_PrecioCamisas();
        }

        public static void Uno_ApruebaCurso() {
            double n1 = Double.parseDouble(JOptionPane.showInputDialog("Ingrese nota 1:"));
            double n2 = Double.parseDouble(JOptionPane.showInputDialog("Ingrese nota 2:"));
            double n3 = Double.parseDouble(JOptionPane.showInputDialog("Ingrese nota 3:"));
            double promedio = (n1 + n2 + n3) / 3;
            if (promedio >= 12) {
                JOptionPane.showMessageDialog(null, "Aprobado");
            } else {
                JOptionPane.showMessageDialog(null, "Reprobado");
            }
        }

        public static void Dos_ParImpar() {
            int num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número:"));
            if (num % 2 == 0) {
                JOptionPane.showMessageDialog(null, "El número es par");
            } else {
                JOptionPane.showMessageDialog(null, "El número es impar");
            }
        }

        public static void Tres_ValorAbsoluto() {
            double num = Double.parseDouble(JOptionPane.showInputDialog("Ingrese un número real:"));
            JOptionPane.showMessageDialog(null, "Valor absoluto: " + Math.abs(num));
        }

        public static void Cuatro_EcuacionSegundoGrado() {
            double a = Double.parseDouble(JOptionPane.showInputDialog("Ingrese A:"));
            double b = Double.parseDouble(JOptionPane.showInputDialog("Ingrese B:"));
            double c = Double.parseDouble(JOptionPane.showInputDialog("Ingrese C:"));
            double discriminante = b * b - 4 * a * c;
            if (a == 0) {
                JOptionPane.showMessageDialog(null, "No es ecuación de segundo grado");
            } else if (discriminante < 0) {
                JOptionPane.showMessageDialog(null, "No tiene soluciones reales");
            } else {
                double x1 = (-b + Math.sqrt(discriminante)) / (2 * a);
                double x2 = (-b - Math.sqrt(discriminante)) / (2 * a);
                JOptionPane.showMessageDialog(null, "Soluciones: x1 = " + x1 + ", x2 = " + x2);
            }
        }

        public static void Cinco_Calculadora() {
            double n1 = Double.parseDouble(JOptionPane.showInputDialog("Ingrese primer número:"));
            String op = JOptionPane.showInputDialog("Ingrese operador (+, -, *, /):");
            double n2 = Double.parseDouble(JOptionPane.showInputDialog("Ingrese segundo número:"));
            double resultado = 0;
            boolean valido = true;
            switch (op) {
                case "+": resultado = n1 + n2; break;
                case "-": resultado = n1 - n2; break;
                case "*": resultado = n1 * n2; break;
                case "/": 
                    if (n2 != 0) resultado = n1 / n2;
                    else { JOptionPane.showMessageDialog(null, "No se puede dividir por cero"); valido = false; }
                    break;
                default: JOptionPane.showMessageDialog(null, "Operador inválido"); valido = false; break;
            }
            if (valido) JOptionPane.showMessageDialog(null, "Resultado: " + resultado);
        }

        public static void Seis_OfertaTienda() {
            int docenas = Integer.parseInt(JOptionPane.showInputDialog("Ingrese cantidad de docenas:"));
            double precioUnitario = Double.parseDouble(JOptionPane.showInputDialog("Ingrese precio por docena:"));
            double montoCompra = docenas * precioUnitario;
            double descuento = (docenas > 3) ? montoCompra * 0.22 : montoCompra * 0.15;
            double montoPagar = montoCompra - descuento;
            int obsequio = (docenas > 3) ? (docenas - 3) : 0;
            JOptionPane.showMessageDialog(null, "Monto compra: " + montoCompra + "\nDescuento: " + descuento + "\nMonto a pagar: " + montoPagar + "\nUnidades de obsequio: " + obsequio);
        }

        public static void Siete_PositivaExpresion() {
            double x = Double.parseDouble(JOptionPane.showInputDialog("Ingrese valor de x:"));
            if (x < -4 || x > 2) {
                JOptionPane.showMessageDialog(null, "Positivo");
            } else {
                JOptionPane.showMessageDialog(null, "No positivo");
            }
        }

        public static void Ocho_NegativaExpresion() {
            double x = Double.parseDouble(JOptionPane.showInputDialog("Ingrese valor de x:"));
            if (x > -3 && x < 4) {
                JOptionPane.showMessageDialog(null, "Negativo");
            } else {
                JOptionPane.showMessageDialog(null, "No negativo");
            }
        }

        public static void Nueve_Temperatura() {
            Double temperatura = Double.parseDouble(JOptionPane.showInputDialog("Temperatura"));
            Double presion = Double.parseDouble(JOptionPane.showInputDialog("Presion"));
            if(temperatura >= 150 || presion <= 380) {
                JOptionPane.showMessageDialog(null, "ALERTA", "ALERTA", JOptionPane.WARNING_MESSAGE);
            } else {
                JOptionPane.showMessageDialog(null, "NORMAL");
            }
        }

        public static void Diez_alumnos(){
            double nota = Double.parseDouble(JOptionPane.showInputDialog("Nota:"));
            int programasResueltos = Integer.parseInt(JOptionPane.showInputDialog("Programas resueltos:"));
            if(nota >= 10.5 && programasResueltos >= 25) {
                JOptionPane.showMessageDialog(null, "Aprobado");
            } else {
                JOptionPane.showMessageDialog(null, "Desaprobado");
            }
        }

        public static void Once_clasificacion() {
            double a = Double.parseDouble(JOptionPane.showInputDialog("Numero 1"));
            double b = Double.parseDouble(JOptionPane.showInputDialog("Numero 2"));
            double c = Double.parseDouble(JOptionPane.showInputDialog("Numero 3"));
            double mayor = a;
            double menor = a;
            if(b > mayor) mayor = b;
            if(c > mayor) mayor = c;
            if(b < menor) menor = b;
            if(c < menor) menor = c;
            JOptionPane.showMessageDialog(null, "El numero mayor es: " + mayor + "\nEl numero menor es: " + menor, "Mayor y Menor", JOptionPane.INFORMATION_MESSAGE);
        }

        public static void Doce_SumaProductoPares(){
            int suma, producto;
            while(true) {
                int a = Integer.parseInt(JOptionPane.showInputDialog("Numero 1"));
                int b = Integer.parseInt(JOptionPane.showInputDialog("Numero 2"));
                if ((a >= 75 && a <= 250) && (b >= 75 && b <= 250) && a%2==0 && b%2==0) {
                    suma = a + b;
                    producto = a*b;
                    JOptionPane.showMessageDialog(null, "La suma es: " + suma + " Y el producto es: " + producto);
                    break;
                } else { 
                    JOptionPane.showMessageDialog(null, "Ingrese numeros pares del 75-250");
                }
            }
        }

        public static void Trece_TrianguloAngulos() {
            int a1 = Integer.parseInt(JOptionPane.showInputDialog("Ángulo 1:"));
            int a2 = Integer.parseInt(JOptionPane.showInputDialog("Ángulo 2:"));
            int a3 = Integer.parseInt(JOptionPane.showInputDialog("Ángulo 3:"));
            int suma = a1 + a2 + a3;
            if (suma == 180) {
                String tipo = "Acutángulo";
                if (a1 == 90 || a2 == 90 || a3 == 90) tipo = "Rectángulo";
                else if (a1 > 90 || a2 > 90 || a3 > 90) tipo = "Obtusángulo";
                JOptionPane.showMessageDialog(null, "Es triángulo. Tipo: " + tipo);
            } else {
                JOptionPane.showMessageDialog(null, "No es triángulo");
            }
        }

        public static void Catorce_Dosnumeros() {
            int a = Integer.parseInt(JOptionPane.showInputDialog("Numero 1"));
            int b = Integer.parseInt(JOptionPane.showInputDialog("Numero 2"));
            int resultado;
            if(a%2 == 0 && b%2 == 0) {
                resultado = a+b;
            } else if (a%2 != 0 && b%2 != 0) {
                resultado = a-b;
            } else {
                resultado = a*b;
            }
            JOptionPane.showMessageDialog(null, "Resultado: " + resultado);
        }

        public static void Quince_PrecioCamisas() {
            int cantidad = Integer.parseInt(JOptionPane.showInputDialog("Cantidad de camisas:"));
            String talla = JOptionPane.showInputDialog("Talla (S, M, L):");
            double precio = 0;
            switch (talla.toUpperCase()) {
                case "S": precio = 55; break;
                case "M": precio = 75; break;
                case "L": precio = 90; break;
                default: JOptionPane.showMessageDialog(null, "Talla inválida"); return;
            }
            double total = cantidad * precio;
            JOptionPane.showMessageDialog(null, "Total a pagar: $" + total);
        }
    }
