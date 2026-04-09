from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

paths = {}

def _handle_PacketIn(event):
    packet = event.parsed
    dpid = event.dpid
    in_port = event.port

    src = packet.src
    dst = packet.dst

    if src not in paths:
        paths[src] = []

    paths[src].append(dpid)

    log.info("Packet from %s at Switch %s", src, dpid)

    if dst in paths:
        log.info("Path to %s: %s", dst, paths[dst])

    # Flood
    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    event.connection.send(msg)

def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    log.info("Path Tracing Started")
