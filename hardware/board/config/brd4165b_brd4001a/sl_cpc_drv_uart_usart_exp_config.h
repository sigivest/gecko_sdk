/***************************************************************************//**
 * @file
 * @brief CPC UART driver configuration file.
 *******************************************************************************
 * # License
 * <b>Copyright 2023 Silicon Laboratories Inc. www.silabs.com</b>
 *******************************************************************************
 *
 * SPDX-License-Identifier: Zlib
 *
 * The licensor of this software is Silicon Laboratories Inc.
 *
 * This software is provided 'as-is', without any express or implied
 * warranty. In no event will the authors be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 *
 ******************************************************************************/

// <<< Use Configuration Wizard in Context Menu >>>

#ifndef SL_CPC_DRV_UART_USART_EXP_CONFIG_H
#define SL_CPC_DRV_UART_USART_EXP_CONFIG_H

// <h> CPC - UART Driver Configuration

// <o SL_CPC_DRV_UART_EXP_RX_QUEUE_SIZE> Number of frame that can be queued in the driver receive queue
// <i> Default: 10
#define SL_CPC_DRV_UART_EXP_RX_QUEUE_SIZE            10

// <o SL_CPC_DRV_UART_EXP_TX_QUEUE_SIZE> Number of frame that can be queued in the driver transmit queue
// <i> Default: 10
#define SL_CPC_DRV_UART_EXP_TX_QUEUE_SIZE            10

// <o SL_CPC_DRV_UART_EXP_BAUDRATE> UART Baudrate
// <i> Default: 115200
#define SL_CPC_DRV_UART_EXP_BAUDRATE              115200

// <o SL_CPC_DRV_UART_EXP_FLOW_CONTROL_TYPE> Flow control
// <usartHwFlowControlNone=> None
// <usartHwFlowControlCtsAndRts=> CTS/RTS
// <i> Default: usartHwFlowControlCtsAndRts
#define SL_CPC_DRV_UART_EXP_FLOW_CONTROL_TYPE usartHwFlowControlCtsAndRts
// </h>

// <<< end of configuration section >>>

// <<< sl:start pin_tool >>>
// <usart signal=TX,RX,(CTS),(RTS)> SL_CPC_DRV_UART_EXP
// $[USART_SL_CPC_DRV_UART_EXP]
#define SL_CPC_DRV_UART_EXP_PERIPHERAL           USART0
#define SL_CPC_DRV_UART_EXP_PERIPHERAL_NO        0

// USART0 TX on PC6
#define SL_CPC_DRV_UART_EXP_TX_PORT              gpioPortC
#define SL_CPC_DRV_UART_EXP_TX_PIN               6
#define SL_CPC_DRV_UART_EXP_TX_LOC               11

// USART0 RX on PC7
#define SL_CPC_DRV_UART_EXP_RX_PORT              gpioPortC
#define SL_CPC_DRV_UART_EXP_RX_PIN               7
#define SL_CPC_DRV_UART_EXP_RX_LOC               11

// USART0 CTS on PB11
#define SL_CPC_DRV_UART_EXP_CTS_PORT             gpioPortB
#define SL_CPC_DRV_UART_EXP_CTS_PIN              11
#define SL_CPC_DRV_UART_EXP_CTS_LOC              2

// USART0 RTS on PF7
#define SL_CPC_DRV_UART_EXP_RTS_PORT             gpioPortF
#define SL_CPC_DRV_UART_EXP_RTS_PIN              7
#define SL_CPC_DRV_UART_EXP_RTS_LOC              26

// [USART_SL_CPC_DRV_UART_EXP]$
// <<< sl:end pin_tool >>>

#endif /* SL_CPC_DRV_UART_EXP_CONFIG_H */
