resource "aws_route53_record" "k8s" {
  zone_id = "Z1033734GXUIGI0YW2PJ"
  name    = "kubernetes.supergoon.com"
  type    = "A"
  ttl     = "300"
  allow_overwrite = true
  alias {
    name                     = aws_elb.main.dns_name
    zone_id                  = aws_elb.main.zone_id
    evaluate_target_health   = true
  }
}